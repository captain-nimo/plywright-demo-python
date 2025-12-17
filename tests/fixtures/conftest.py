import pytest
from playwright.async_api import async_playwright, Browser, BrowserContext, Page
from config.settings import get_config
from utils.logger import Logger
from utils.helpers import Helpers


config = get_config()
logger = Logger.get_logger()


@pytest.fixture(scope="function")
async def browser():
    """Create a browser instance for each test"""
    logger.info(f"Starting browser: {config.BROWSER}")

    async with async_playwright() as p:
        browser = (
            await p.chromium.launch(**config.get_browser_launch_args())
            if config.BROWSER == "chromium"
            else (
                await p.firefox.launch(**config.get_browser_launch_args())
                if config.BROWSER == "firefox"
                else await p.webkit.launch(**config.get_browser_launch_args())
            )
        )

        yield browser

        logger.info("Closing browser")
        await browser.close()


@pytest.fixture(scope="function")
async def context(browser: Browser):
    """Create a browser context"""
    logger.debug("Creating new browser context")

    context = await browser.new_context(**config.get_context_options())

    yield context

    logger.debug("Closing browser context")
    await context.close()


@pytest.fixture(scope="function")
async def page(context: BrowserContext):
    """Create a new page"""
    logger.debug("Creating new page")

    page = await context.new_page()
    page.set_default_timeout(config.DEFAULT_TIMEOUT)
    page.set_default_navigation_timeout(config.NAVIGATION_TIMEOUT)

    yield page

    logger.debug("Closing page")
    await page.close()


@pytest.fixture
def sync_browser():
    """Create a synchronous browser instance"""
    from playwright.sync_api import sync_playwright

    logger.info(f"Starting sync browser: {config.BROWSER}")

    with sync_playwright() as p:
        if config.BROWSER == "chromium":
            browser = p.chromium.launch(**config.get_browser_launch_args())
        elif config.BROWSER == "firefox":
            browser = p.firefox.launch(**config.get_browser_launch_args())
        else:
            browser = p.webkit.launch(**config.get_browser_launch_args())

        yield browser

        logger.info("Closing sync browser")
        browser.close()


@pytest.fixture
def sync_context(sync_browser):
    """Create a synchronous browser context"""
    logger.debug("Creating new sync browser context")

    context = sync_browser.new_context(**config.get_context_options())

    yield context

    logger.debug("Closing sync browser context")
    context.close()


@pytest.fixture
def sync_page(sync_context):
    """Create a synchronous page"""
    logger.debug("Creating new sync page")

    page = sync_context.new_page()
    page.set_default_timeout(config.DEFAULT_TIMEOUT)
    page.set_default_navigation_timeout(config.NAVIGATION_TIMEOUT)

    yield page

    logger.debug("Closing sync page")
    page.close()


@pytest.fixture
def test_data():
    """Provide test data"""
    return {
        "valid_url": "https://example.com",
        "invalid_url": "https://invalid-url-12345.example.com",
        "timeout": config.DEFAULT_TIMEOUT,
    }


# Pytest markers
def pytest_configure(config):
    """Register custom markers"""
    config.addinivalue_line("markers", "ui: mark test as UI automation test")
    config.addinivalue_line("markers", "api: mark test as API automation test")
    config.addinivalue_line("markers", "slow: mark test as slow")
    config.addinivalue_line("markers", "smoke: mark test as smoke test")
