"""
HTML Page Object Model

Demonstrates the Page Object Model pattern with interactions on httpbin.org HTML page.
"""

from tests.ui.pages.base_page import BasePage
from utils.logger import Logger


logger = Logger.get_logger()


class HtmlPage(BasePage):
    """HTML page object for httpbin.org/html"""

    # Locators
    HEADING = "h1"
    PARAGRAPH = "p"
    LINK = "a"

    def __init__(self, page, base_url: str = "https://httpbin.org/html"):
        """Initialize HTML page"""
        super().__init__(page, base_url)

    def get_heading_text(self) -> str:
        """Get page heading text"""
        logger.debug("Getting heading text")
        return self.page.text_content(self.HEADING)

    def get_paragraph_text(self) -> str:
        """Get paragraph text"""
        logger.debug("Getting paragraph text")
        return self.page.text_content(self.PARAGRAPH)

    def get_all_links(self) -> list:
        """Get all links on page"""
        logger.debug("Getting all links")
        locator = self.page.locator(self.LINK)
        return [locator.nth(i).get_attribute("href") for i in range(locator.count())]

    def click_link(self, link_text: str):
        """Click link by text"""
        logger.debug(f"Clicking link: {link_text}")
        self.page.click(f"text={link_text}")

    def get_page_url(self) -> str:
        """Get current page URL"""
        logger.debug("Getting page URL")
        return self.page.url
