from playwright.sync_api import Page
from utils.logger import Logger


logger = Logger.get_logger()


class BasePage:
    """Base page class with common methods for all pages"""

    def __init__(self, page: Page, base_url: str):
        """
        Initialize the page

        Args:
            page: Playwright Page object
            base_url: Base URL for navigation
        """
        self.page = page
        self.base_url = base_url

    def navigate(self, path: str = ""):
        """Navigate to a URL"""
        url = self.base_url + path
        logger.info(f"Navigating to: {url}")
        self.page.goto(url)

    def wait_for_load_state(self, state: str = "networkidle"):
        """Wait for the page to load"""
        logger.debug(f"Waiting for page to reach '{state}' state")
        self.page.wait_for_load_state(state)

    def wait_for_selector(self, selector: str, timeout: int = 30000):
        """Wait for an element to be visible"""
        logger.debug(f"Waiting for selector: {selector}")
        self.page.wait_for_selector(selector, timeout=timeout)

    def click(self, selector: str):
        """Click an element"""
        logger.debug(f"Clicking element: {selector}")
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        """Fill the input field"""
        logger.debug(f"Filling '{selector}' with text: {text}")
        self.page.fill(selector, text)

    def type_text(self, selector: str, text: str, delay: int = 0):
        """Type text character by character"""
        logger.debug(f"Typing text in '{selector}'")
        self.page.type(selector, text, delay=delay)

    def get_text(self, selector: str) -> str:
        """Get text content of an element"""
        logger.debug(f"Getting text from: {selector}")
        return self.page.text_content(selector)

    def get_attribute(self, selector: str, attribute: str) -> str:
        """Get attribute value of an element"""
        logger.debug(f"Getting attribute '{attribute}' from: {selector}")
        return self.page.get_attribute(selector, attribute)

    def is_visible(self, selector: str) -> bool:
        """Check if an element is visible"""
        try:
            return self.page.is_visible(selector)
        except Exception as e:
            logger.warning(f"Error checking visibility of {selector}: {e}")
            return False

    def is_enabled(self, selector: str) -> bool:
        """Check if an element is enabled"""
        try:
            return self.page.is_enabled(selector)
        except Exception as e:
            logger.warning(f"Error checking if {selector} is enabled: {e}")
            return False

    def select_option(self, selector: str, value: str):
        """Select option from dropdown"""
        logger.debug(f"Selecting '{value}' from dropdown: {selector}")
        self.page.select_option(selector, value)

    def take_screenshot(self, filename: str) -> str:
        """Take a screenshot and save to file"""
        logger.info(f"Taking screenshot: {filename}")
        return self.page.screenshot(path=filename)

    def get_url(self) -> str:
        """Get current page URL"""
        return self.page.url

    def get_title(self) -> str:
        """Get page title"""
        return self.page.title()

    def reload(self):
        """Reload page"""
        logger.info("Reloading page")
        self.page.reload()

    def go_back(self):
        """Go back to the previous page"""
        logger.info("Going back")
        self.page.go_back()

    def go_forward(self):
        """Go forward to the next page"""
        logger.info("Going forward")
        self.page.go_forward()

    def close(self):
        """Close the page"""
        logger.info("Closing page")
        self.page.close()
