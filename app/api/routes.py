import time
import structlog
from fastapi import APIRouter, HTTPException
from typing import List

from app.config import settings
from app.models.schemas import (
    AnalysisRequest,
    AnalysisResponse,
    Platform
)
from app.services.platform_detector import PlatformDetector
from app.services.scraper_service import ScraperService
from app.services.sentiment_service import SentimentService
from app.utils.batch_processor import BatchProcessor

logger = structlog.get_logger()
router = APIRouter()

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_url(request: AnalysisRequest) -> AnalysisResponse:
    """Analyze sentiment of comments on a social media post."""
    start_time = time.time()
    
    try:
        # Detect platform from URL string
        url_str = str(request.url)
        platform = PlatformDetector.detect_platform(url_str)
        
        # Scrape content
        scraper = ScraperService()
        post_context, comments = await scraper.scrape_platform(url_str, platform)
        
        # Truncate comments if needed
        if len(comments) > settings.MAX_COMMENTS:
            comments = comments[:settings.MAX_COMMENTS]
            logger.info("truncated_comments",
                       original_count=len(comments),
                       truncated_to=settings.MAX_COMMENTS)
        
        # Analyze sentiments
        sentiment_service = SentimentService()
        
        # Process in batches
        batch_processor = BatchProcessor()
        from app.utils.comment_cleaner import CommentCleaner
        batches = CommentCleaner.chunk_comments(
            comments,
            settings.BATCH_SIZE
        )
        
        # Create a partial function to include the URL
        from functools import partial
        analyze_func = partial(
            sentiment_service.analyze_batch_with_gemini,
            url=url_str
        )
        
        batch_results = await batch_processor.process_batches_parallel(
            batches,
            analyze_func,
            post_context,
            settings.MAX_CONCURRENT_BATCHES
        )
        
        # Merge results
        all_sentiments = batch_processor.merge_batch_results(batch_results)
        
        # Calculate total processing time
        processing_time = time.time() - start_time
        
        # Create response
        response = sentiment_service.create_summary_response(
            post_url=url_str,
            platform=platform,
            sentiments=all_sentiments,
            processing_time=processing_time,
            batches_count=len(batch_results)
        )
        
        logger.info("analysis_complete",
                   url=url_str,
                   platform=platform.value,
                   total_comments=len(all_sentiments),
                   processing_time=processing_time)
                   
        return response
        
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except Exception as e:
        logger.error("analysis_error",
                    url=request.url,
                    error=str(e))
        raise HTTPException(
            status_code=500,
            detail="Internal server error during analysis"
        )

@router.get("/analyze/demo", response_model=AnalysisResponse)
async def get_demo_analysis() -> AnalysisResponse:
    """Return a sample analysis response for demonstration."""
    from datetime import datetime
    from app.models.schemas import SentimentSummary
    
    summary = SentimentSummary(
        totalComments=3,
        supportive_empathetic=1,
        critical_disapproving=0,
        angry_hostile=0,
        sarcastic_ironic=1,
        informative_neutral=1,
        appreciative_praising=0
    )
    
    return AnalysisResponse(
        status="completed",
        timestamp=datetime.now(),
        postUrl="https://www.youtube.com/watch?v=demo",
        platform=Platform.YOUTUBE,
        summary=summary,
        topComments={
            "Supportive/Empathetic": ["Great explanation! Very helpful."],
            "Sarcastic/Ironic": ["Oh sure, like that's going to work..."],
            "Informative/Neutral": ["The video was released on June 1st."]
        },
        allComments={
            "Supportive/Empathetic": ["Great explanation! Very helpful."],
            "Sarcastic/Ironic": ["Oh sure, like that's going to work..."],
            "Informative/Neutral": ["The video was released on June 1st."]
        },
        processingTime=0.5,
        batchesProcessed=1
    )

@router.get("/platforms")
async def get_supported_platforms() -> dict:
    """Get list of supported platforms and their limits."""
    return {
        "platforms": [
            {
                "name": Platform.YOUTUBE.value,
                "maxComments": settings.YOUTUBE_MAX_COMMENTS,
                "example": "https://www.youtube.com/watch?v=xxxxx"
            },
            {
                "name": Platform.FACEBOOK.value,
                "maxComments": settings.FACEBOOK_MAX_COMMENTS,
                "example": "https://www.facebook.com/user/posts/xxxxx"
            },
            {
                "name": Platform.TWITTER.value,
                "maxComments": settings.TWITTER_MAX_ITEMS,
                "example": "https://twitter.com/user/status/xxxxx"
            },
            {
                "name": Platform.INSTAGRAM.value,
                "maxComments": settings.INSTAGRAM_MAX_COMMENTS,
                "example": "https://www.instagram.com/p/xxxxx"
            }
        ]
    }
