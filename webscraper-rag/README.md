# WebScraper RAG

A web scraping Retrieval-Augmented Generation app with:
- `backend/` FastAPI + Playwright crawler
- `backend/chunker.py` LangChain text splitter + embeddings
- `backend/vectorstore.py` ChromaDB vector store
- `backend/qa.py` LangChain RetrievalQA
- `frontend/` React + Vite app

## Setup

### 1. Backend

From `webscraper-rag/backend`:

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m playwright install
```

Create a `.env` file in `backend/` with your OpenAI key:

```env
OPENAI_API_KEY=your_openai_api_key
USE_GROQ=false
```

If you want to use Groq embeddings instead of OpenAI, set `USE_GROQ=true` and install the compatible Groq packages.

Start the backend:

```bash
uvicorn backend.main:app --reload
```

The API runs on `http://localhost:8000`.

### 2. Frontend

From `webscraper-rag/frontend`:

```bash
npm install
npm run dev
```

Open the URL shown by Vite (usually `http://localhost:5173`).

## Usage

1. Enter a page URL in the frontend and click **Crawl & Index**.
2. Wait until the page text is scraped and indexed.
3. Ask a question about the crawled page with **Ask AI**.

## Architecture

- `backend/main.py`: API routes for crawl and query
- `backend/crawler.py`: Playwright headless page scraper
- `backend/chunker.py`: text splitting and embeddings
- `backend/vectorstore.py`: ChromaDB persistence and upsert
- `backend/qa.py`: LangChain RetrievalQA chain
- `frontend/`: Vite React UI for user input and answers

## Notes

- You can extend the backend with authentication, page filtering, or multi-page batch crawls.
- The current frontend uses a simple `fetch` wrapper and can be improved with loading states and history.
