import { useState } from 'react';
import './App.css';

const API_BASE = 'http://localhost:8000';

function App() {
  const [url, setUrl] = useState('');
  const [question, setQuestion] = useState('');
  const [message, setMessage] = useState('');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);

  const crawl = async () => {
    setLoading(true);
    setMessage('Crawling URL and indexing text...');
    setAnswer('');
    try {
      const response = await fetch(`${API_BASE}/crawl`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || 'Crawl failed');
      setMessage(`Indexed ${data.chunks} chunks from ${data.url}`);
    } catch (error) {
      setMessage(`Error: ${error}`);
    } finally {
      setLoading(false);
    }
  };

  const ask = async () => {
    setLoading(true);
    setMessage('Querying indexed content...');
    try {
      const response = await fetch(`${API_BASE}/query`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || 'Query failed');
      setAnswer(data.answer);
      setMessage('Answer received');
    } catch (error) {
      setMessage(`Error: ${error}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="card">
        <h1>WebScraper RAG</h1>
        <label>
          Page URL
          <input
            type="url"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="https://example.com"
          />
        </label>
        <button onClick={crawl} disabled={loading || !url}>
          Crawl & Index
        </button>

        <label>
          Question
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask about the crawled page"
          />
        </label>
        <button onClick={ask} disabled={loading || !question}>
          Ask AI
        </button>

        <div className="status">
          <p>{message}</p>
          {answer && (
            <div>
              <strong>Answer</strong>
              <p>{answer}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
