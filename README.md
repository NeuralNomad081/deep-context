# Deep Context Sentiment Analysis

A production-ready sentiment analysis system that processes social media comments in real-time with a modern dashboard UI. The system uses Google's Gemini AI for advanced contextual sentiment analysis and supports multiple social media platforms.

## Features

- Real-time sentiment analysis of social media comments
- Support for YouTube, Facebook, Twitter, and Instagram
- Advanced contextual analysis using Google Gemini AI
- Modern React dashboard with interactive visualizations
- Docker containerization for easy deployment
- Comprehensive test suite with high coverage
- Production-ready configuration

## Tech Stack

### Backend
- FastAPI with async/await
- Google Gemini for sentiment analysis
- httpx for async API calls
- Pydantic v2 for data validation
- structlog for logging
- pytest for testing

### Frontend
- React 18+ with TypeScript
- Tailwind CSS + shadcn/ui
- Recharts for data visualization
- Framer Motion for animations

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local development)
- Node.js 18+ (for frontend development)

### Environment Setup

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd deep-context-sentiment-analysis
   ```

2. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

3. Update the environment variables in `.env`:
   ```bash
   GOOGLE_GEMINI_API_KEY=your_api_key
   APIFY_API_TOKEN=your_token
   ```

### Running with Docker

1. Build and start the containers:
   ```bash
   docker compose up --build
   ```

2. Access the services:
   - Backend API: http://localhost:8000
   - Frontend Dashboard: http://localhost:3000
   - API Documentation: http://localhost:8000/docs

### Local Development

1. Backend Setup:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

2. Frontend Setup:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## API Documentation

### Endpoints

- `POST /api/v1/analyze`
  - Analyze sentiment from a social media URL
  - Returns detailed sentiment analysis

- `GET /api/v1/analyze/demo`
  - Returns sample analysis response
  - Useful for frontend development

- `GET /api/v1/platforms`
  - List supported platforms and their limits

### Example Request

```bash
curl -X POST http://localhost:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=example"}'
```

## Testing

### Backend Tests

```bash
pytest tests/ --cov=app
```

### Frontend Tests

```bash
cd frontend
npm test
```

## Performance

- Scraping: 2-5 seconds
- Batch Analysis (100 comments): 6-10 seconds
- Total Response Time: 8-16 seconds
- Error Rate: <5%
- Batch Success Rate: >95%

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Gemini AI for sentiment analysis
- Apify for social media scraping
- The FastAPI and React communities
