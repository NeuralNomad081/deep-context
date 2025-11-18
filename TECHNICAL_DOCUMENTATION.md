# Technical Documentation

## Introduction

This document provides a technical overview of the Deep Context Sentiment Analysis project. It is intended for developers who want to contribute to the project or understand its inner workings.

## Project Structure

```
.
├── Dockerfile
├── PROJECT_STRUCTURE.md
├── README.md
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── config.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   └── schemas.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── platform_detector.py
│   │   ├── scraper_service.py
│   │   └── sentiment_service.py
│   └── utils
│       ├── __init__.py
│       ├── ai_agent_logger.py
│       ├── batch_processor.py
│       ├── comment_cleaner.py
│       └── json_parser.py
├── docker-compose.yml
├── frontend
│   ├── Dockerfile
│   └── deep-context-dashboard
│       ├── README.md
│       ├── package-lock.json
│       ├── package.json
│       ├── postcss.config.js
│       ├── public
│       ├── src
│       └── tailwind.config.js
├── render.yml
├── requirements.txt
└── social_sentiment.yml
```

## Technologies Used

### Backend

*   **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
*   **Google Gemini AI**: Used for contextual sentiment analysis.
*   **httpx**: A fully featured HTTP client for Python 3, which provides sync and async APIs, and support for both HTTP/1.1 and HTTP/2.
*   **Pydantic v2**: Data validation and settings management using Python type annotations.
*   **structlog**: Structured logging for Python.
*   **pytest**: A mature full-featured Python testing tool.
*   **Apify**: A web scraping and automation platform.

### Frontend

*   **React**: A JavaScript library for building user interfaces.
*   **Axios**: A promise-based HTTP client for the browser and Node.js.
*   **Framer Motion**: A production-ready motion library for React.
*   **Lucide React**: A simple and beautiful icon library for React.
*   **Recharts**: A composable charting library built on React components.
*   **Tailwind CSS**: A utility-first CSS framework for rapidly building custom designs.

### DevOps

*   **Docker**: A platform for developing, shipping, and running applications in containers.
*   **Docker Compose**: A tool for defining and running multi-container Docker applications.

## API Endpoints

### `POST /api/v1/analyze`

Analyzes sentiment from a social media URL.

*   **Input**: `{"url": "https://platform.com/post"}`
*   **Returns**: A detailed sentiment analysis with an overall sentiment summary, per-comment analysis with justifications, and processing metrics.

### `GET /api/v1/analyze/demo`

Returns a sample analysis response for testing and development purposes.

### `GET /api/v1/platforms`

Lists the supported social media platforms and their limits, including example URLs and rate limits.

## How to Contribute

1.  Fork the repository.
2.  Create a feature branch.
3.  Commit your changes.
4.  Push to the branch.
5.  Open a Pull Request.

## Further Explanation

The project is divided into two main components: a backend FastAPI application and a frontend React application. The backend is responsible for handling API requests, scraping social media content, analyzing sentiment using Google's Gemini AI, and returning the results. The frontend provides a user-friendly dashboard to interact with the API and visualize the sentiment analysis results. Both components are containerized using Docker for easy deployment.
