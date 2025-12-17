from typing import Dict

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config.settings import get_config
from utils.logger import Logger

logger = Logger.get_logger()
config = get_config()


class APIClient:
    """Base API client with common methods"""

    def __init__(self, base_url: str = None, timeout: int = None, headers: Dict = None):
        """
        Initialize API client

        Args:
            base_url: Base URL for API
            timeout: Request timeout in seconds
            headers: Additional headers
        """
        self.base_url = base_url or config.API_BASE_URL
        self.timeout = timeout or config.API_TIMEOUT
        self.session = requests.Session()

        # Set default headers
        self.session.headers.update(
            {
                "User-Agent": "Playwright-Demo/1.0",
                "Accept": "application/json",
            }
        )

        # Add custom headers if provided
        if headers:
            self.session.headers.update(headers)

        # Setup retry strategy
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        logger.info(f"Initialized API client with base URL: {self.base_url}")

    def _build_url(self, endpoint: str) -> str:
        """Build full URL from the endpoint"""
        if endpoint.startswith("http"):
            return endpoint
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def get(self, endpoint: str, params: Dict = None, **kwargs) -> requests.Response:
        """Make a GET request"""
        url = self._build_url(endpoint)
        logger.info(f"GET {url}")

        try:
            response = self.session.get(url, params=params, timeout=self.timeout, **kwargs)
            logger.debug(f"Response status: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"GET request failed: {e}")
            raise

    def post(
        self, endpoint: str, data: Dict = None, json_data: Dict = None, **kwargs
    ) -> requests.Response:
        """Make a POST request"""
        url = self._build_url(endpoint)
        logger.info(f"POST {url}")

        try:
            response = self.session.post(
                url, data=data, json=json_data, timeout=self.timeout, **kwargs
            )
            logger.debug(f"Response status: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"POST request failed: {e}")
            raise

    def put(
        self, endpoint: str, data: Dict = None, json_data: Dict = None, **kwargs
    ) -> requests.Response:
        """Make a PUT request"""
        url = self._build_url(endpoint)
        logger.info(f"PUT {url}")

        try:
            response = self.session.put(
                url, data=data, json=json_data, timeout=self.timeout, **kwargs
            )
            logger.debug(f"Response status: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"PUT request failed: {e}")
            raise

    def patch(
        self, endpoint: str, data: Dict = None, json_data: Dict = None, **kwargs
    ) -> requests.Response:
        """Make PATCH request"""
        url = self._build_url(endpoint)
        logger.info(f"PATCH {url}")

        try:
            response = self.session.patch(
                url, data=data, json=json_data, timeout=self.timeout, **kwargs
            )
            logger.debug(f"Response status: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"PATCH request failed: {e}")
            raise

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """Make DELETE request"""
        url = self._build_url(endpoint)
        logger.info(f"DELETE {url}")

        try:
            response = self.session.delete(url, timeout=self.timeout, **kwargs)
            logger.debug(f"Response status: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"DELETE request failed: {e}")
            raise

    def set_auth_header(self, token: str, header_type: str = "Bearer"):
        """Set authorization header"""
        self.session.headers["Authorization"] = f"{header_type} {token}"
        logger.debug(f"Authorization header set with type: {header_type}")

    def set_header(self, key: str, value: str):
        """Set a custom header"""
        self.session.headers[key] = value
        logger.debug(f"Header set: {key} = {value}")

    def close(self):
        """Close the session"""
        logger.info("Closing API client session")
        self.session.close()

    def __enter__(self):
        """Context manager entry"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()
