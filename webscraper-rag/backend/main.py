import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from .crawler import fetch_page_text
from .chunker import split_text
from .vectorstore import upsert_texts
from .qa import answer_question

app = FastAPI(title="WebScraper RAG", version="0.1.0")


class CrawlRequest(BaseModel):
    url: HttpUrl


class QueryRequest(BaseModel):
    question: str


@app.post("/crawl")
async def crawl_url(payload: CrawlRequest):
    text = await fetch_page_text(str(payload.url))
    if not text:
        raise HTTPException(status_code=400, detail="Unable to extract page text")

    chunks = split_text(text)
    if not chunks:
        raise HTTPException(status_code=400, detail="No text chunks produced")

    metadatas = [{"source": str(payload.url), "chunk_index": idx} for idx in range(len(chunks))]
    upsert_texts(texts=chunks, metadatas=metadatas)
    return {"status": "ok", "url": str(payload.url), "chunks": len(chunks)}


@app.post("/query")
def ask_question(payload: QueryRequest):
    answer = answer_question(payload.question)
    return {"question": payload.question, "answer": answer}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
