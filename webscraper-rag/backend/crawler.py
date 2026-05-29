from playwright.async_api import async_playwright
from typing import Optional

async def fetch_page_text(url: str, timeout: int = 30000) -> str:
    """Open a page with Playwright and return the visible body text."""
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, timeout=timeout)
        content = await page.text_content("body") or ""
        await browser.close()
    return content.strip()
