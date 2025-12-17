"""
Example UI Automation Tests

This module demonstrates UI automation using Playwright with the Page Object Model pattern.
Tests showcase common browser automation scenarios.
"""

import pytest
from utils.logger import Logger


logger = Logger.get_logger()


@pytest.mark.ui
class TestExampleUI:
    """Example UI automation tests"""

    @pytest.mark.smoke
    async def test_navigate_to_page(self, page):
        """Test basic page navigation"""
        logger.info("Starting test: test_navigate_to_page")

        # Navigate to the example page
        await page.goto("https://httpbin.org/html")

        # Verify page loaded by checking URL
        assert "httpbin.org" in page.url

        logger.info("✓ Successfully navigated to page")

    @pytest.mark.smoke
    async def test_check_page_heading(self, page):
        """Test page heading verification"""
        logger.info("Starting test: test_check_page_heading")

        await page.goto("https://httpbin.org/html")

        # Wait for h1 heading
        heading_locator = page.locator("h1")
        await heading_locator.wait_for()

        # Get heading text
        heading_text = await heading_locator.text_content()
        assert "Moby" in heading_text and "Dick" in heading_text

        logger.info(f"✓ Found heading: {heading_text}")

    @pytest.mark.smoke
    async def test_check_page_content(self, page):
        """Test page content verification"""
        logger.info("Starting test: test_check_page_content")

        await page.goto("https://httpbin.org/html")

        # Check for paragraph content - use first() to get specific element
        paragraph_locator = page.locator("p").first
        await paragraph_locator.wait_for()

        paragraph_text = await paragraph_locator.text_content()
        assert len(paragraph_text) > 0

        logger.info(f"✓ Found paragraph content")

    async def test_take_screenshot(self, page):
        """Test taking screenshots"""
        logger.info("Starting test: test_take_screenshot")

        await page.goto("https://httpbin.org/html")
        await page.wait_for_load_state("networkidle")

        # Take screenshot
        screenshot_path = "test-results/screenshots/example_page.png"
        await page.screenshot(path=screenshot_path)

        logger.info(f"✓ Screenshot saved: {screenshot_path}")

    @pytest.mark.slow
    async def test_page_response_time(self, page):
        """Test page load time"""
        logger.info("Starting test: test_page_response_time")

        import time

        start_time = time.time()
        await page.goto("https://httpbin.org/html", wait_until="networkidle")
        load_time = time.time() - start_time

        # Assert page loaded in a reasonable time (adjust a threshold as needed)
        assert load_time < 10, f"Page took {load_time:.2f}s to load"

        logger.info(f"✓ Page loaded in {load_time:.2f}s")


class TestExampleUISync:
    """Example synchronous UI automation tests"""

    @pytest.mark.ui
    @pytest.mark.smoke
    def test_sync_navigate_to_page(self, sync_page):
        """Test basic synchronous page navigation"""
        logger.info("Starting test: test_sync_navigate_to_page")

        # Navigate to the example page
        sync_page.goto("https://example.com")

        # Verify page title
        title = sync_page.title()
        assert "Example" in title

        logger.info("✓ Sync navigation test passed")

    @pytest.mark.ui
    @pytest.mark.smoke
    def test_sync_check_heading(self, sync_page):
        """Test synchronous heading verification"""
        logger.info("Starting test: test_sync_check_heading")

        sync_page.goto("https://example.com")

        # Get heading text
        heading_text = sync_page.locator("h1").text_content()
        assert "Example Domain" in heading_text

        logger.info(f"✓ Found heading: {heading_text}")

    @pytest.mark.ui
    def test_sync_page_elements_count(self, sync_page):
        """Test element count on the page"""
        logger.info("Starting test: test_sync_page_elements_count")

        sync_page.goto("https://example.com")

        # Count paragraphs
        paragraphs = sync_page.locator("p")
        count = paragraphs.count()
        assert count > 0

        logger.info(f"✓ Found {count} paragraph(s) on page")
