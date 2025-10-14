from functools import lru_cache
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API Configuration
    APP_NAME: str = "Sentiment Analyzer API"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # API Keys
    APIFY_API_TOKEN: str
    GOOGLE_GEMINI_API_KEY: str
    OPENAI_API_KEY: Optional[str] = None
    
    # Model Configuration
    GEMINI_MODEL: str = "gemini-2.5-flash-lite"
    OPENAI_MODEL: Optional[str] = "gpt-4"
    
    # Processing Settings
    BATCH_SIZE: int = 10
    MAX_COMMENTS: int = 100
    MAX_CONCURRENT_BATCHES: int = 5
    REQUEST_TIMEOUT: int = 300
    
    # Platform Specific Limits
    YOUTUBE_MAX_COMMENTS: int = 100
    FACEBOOK_MAX_COMMENTS: int = 100
    TWITTER_MAX_ITEMS: int = 100
    INSTAGRAM_MAX_COMMENTS: int = 100
    
    # Optional Integrations
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: Optional[str] = None
    
    GOOGLE_SHEETS_CREDENTIALS_FILE: str = "credentials.json"
    GOOGLE_SHEETS_SPREADSHEET_ID: Optional[str] = None
    GOOGLE_SHEETS_SHEET_NAME: str = "Sheet1"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Create cached settings instance."""
    return Settings()


settings = get_settings()