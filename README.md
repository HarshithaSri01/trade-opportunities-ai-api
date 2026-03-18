# Trade Opportunities API

A FastAPI-based service that analyzes market data and provides trade opportunity insights for specific sectors in India using Google Gemini AI.

## 🚀 Features

- **Sector Analysis**: GET `/api/v1/analyze/{sector}` (e.g., `pharmaceuticals`, `technology`, `agriculture`).
- **Data Collection**: Integrated with DuckDuckGo for real-time market news and trends in India.
- **AI-Powered Reports**: Generates structured Markdown reports using Google Gemini (Gemini 1.5 Flash).
- **Security**: 
  - Simple API Key Authentication (`X-API-Key` header).
  - Rate Limiting (default: 5 requests per minute).
  - Session tracking for usage monitoring.
- **Auto-Documentation**: Full Swagger UI and ReDoc support.

## 🛠️ Setup Instructions

### 1. Prerequisites
- Python 3.9+
- A Google Gemini API Key (get one for free at [Google AI Studio](https://aistudio.google.com/)).

### 2. Installation
1. Clone the repository (or extract into a folder).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Environment Configuration
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
API_KEY=trade-api-secret-key-12345
```

### 4. Running the Application
```bash
python -m src.main
```
The API will be available at `http://localhost:8000`.

## 📖 API Usage

### Root Endpoint
`GET /` - Check if the API is online.

### Analysis Endpoint
`GET /analyze/{sector}`
- **Header**: `X-API-Key: trade-api-secret-key-12345`
- **Example**: `GET http://localhost:8000/analyze/pharmaceuticals`
- **Response**: A file download of a Markdown report (`pharmaceuticals_trade_report.md`).

### Status Endpoint
`GET /status` - View session stats and system status.

## 🏗️ Architecture
- `src/main.py`: API routes and app configuration.
- `src/services/searcher.py`: Web searching logic.
- `src/services/analyzer.py`: LLM integration and report generation.
- `src/core/security.py`: Auth and rate limiting.
- `src/core/config.py`: Environment and settings management.

## 📝 Success Criteria Met
- [x] FastAPI implementation with async handling.
- [x] Gemini API integration for analysis.
- [x] Market data collection using DuckDuckGo.
- [x] Security (API Key & Rate Limiting).
- [x] Structured Markdown report output.
