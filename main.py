"""
Playwright Demo - Quick Start Example

This script demonstrates basic Playwright usage for UI and API automation.
Run this to verify your setup is working correctly.
"""

import asyncio
from playwright.async_api import async_playwright
import requests
from utils.logger import Logger
from config.settings import get_config


logger = Logger.get_logger()
config = get_config()


async def demo_ui_automation():
    """Demonstrate UI automation with Playwright"""
    logger.info("=" * 50)
    logger.info("Starting UI Automation Demo")
    logger.info("=" * 50)

    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        try:
            # Navigate to Example Domain
            logger.info("Navigating to https://example.com")
            await page.goto("https://example.com")

            # Wait for content to load
            await page.wait_for_load_state("networkidle")

            # Get page title
            title = await page.title()
            logger.info(f"✓ Page title: {title}")

            # Get heading
            heading = await page.text_content("h1")
            logger.info(f"✓ Page heading: {heading}")

            # Get paragraph content
            paragraph = await page.text_content("p")
            logger.info(f"✓ Page content preview: {paragraph[:50]}...")

            # Take screenshot
            await page.screenshot(path="test-results/screenshots/demo_ui.png")
            logger.info("✓ Screenshot saved to test-results/screenshots/demo_ui.png")

            logger.info("✓ UI Automation Demo completed successfully!")

        finally:
            await context.close()
            await browser.close()


def demo_api_automation():
    """Demonstrate API automation with requests"""
    logger.info("")
    logger.info("=" * 50)
    logger.info("Starting API Automation Demo")
    logger.info("=" * 50)

    api_base_url = "https://jsonplaceholder.typicode.com"

    try:
        # GET request
        logger.info(f"Making GET request to {api_base_url}/posts/1")
        response = requests.get(f"{api_base_url}/posts/1", timeout=10)

        if response.status_code == 200:
            post = response.json()
            logger.info(f"✓ Status Code: {response.status_code}")
            logger.info(f"✓ Post ID: {post['id']}")
            logger.info(f"✓ Post Title: {post['title'][:50]}...")
        else:
            logger.error(f"✗ Request failed with status {response.status_code}")
            return

        # POST request
        logger.info(f"\nMaking POST request to {api_base_url}/posts")
        new_post = {
            "title": "Playwright Demo Post",
            "body": "This is a demo post created by Playwright",
            "userId": 1,
        }

        response = requests.post(f"{api_base_url}/posts", json=new_post, timeout=10)

        if response.status_code == 201:
            created_post = response.json()
            logger.info(f"✓ Status Code: {response.status_code}")
            logger.info(f"✓ Created Post ID: {created_post['id']}")
            logger.info(f"✓ Created Post Title: {created_post['title']}")
        else:
            logger.error(f"✗ Request failed with status {response.status_code}")
            return

        logger.info("✓ API Automation Demo completed successfully!")

    except requests.exceptions.RequestException as e:
        logger.error(f"✗ API request failed: {e}")


def main():
    """Main entry point"""
    logger.info("🎭 Playwright Python Demo - Quick Start")
    logger.info(f"Config Environment: {config.LOG_LEVEL}")

    # Create test-results directory
    from utils.helpers import Helpers

    Helpers.ensure_screenshot_dir()

    # Run UI demo
    asyncio.run(demo_ui_automation())

    # Run API demo
    demo_api_automation()

    logger.info("")
    logger.info("=" * 50)
    logger.info("✨ All demos completed successfully!")
    logger.info("=" * 50)
    logger.info("\nNext steps:")
    logger.info("1. Run tests: pytest tests/")
    logger.info("2. Run UI tests: pytest tests/ui/")
    logger.info("3. Run API tests: pytest tests/api/")
    logger.info("4. Run with parallel: pytest -n auto")
    logger.info("5. Generate HTML report: pytest --html=report.html --self-contained-html")


if __name__ == "__main__":
    main()
