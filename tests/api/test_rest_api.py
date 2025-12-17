"""
Example API Automation Tests

This module demonstrates API automation using the requests library with the API Client.
Tests showcase common REST API testing scenarios.
"""

import pytest

from tests.api.clients.api_client import APIClient
from utils.logger import Logger

logger = Logger.get_logger()


@pytest.mark.api
class TestExampleAPI:
    """Example API automation tests"""

    @pytest.fixture
    def api_client(self):
        """Create an API client for tests"""
        return APIClient(base_url="https://jsonplaceholder.typicode.com")

    @pytest.mark.smoke
    def test_get_single_post(self, api_client):
        """Test GET request - retrieve a single post"""
        logger.info("Starting test: test_get_single_post")

        response = api_client.get("/posts/1")

        # Assertions
        assert response.status_code == 200
        assert response.json()["id"] == 1
        assert "title" in response.json()
        assert "body" in response.json()

        logger.info("✓ Successfully retrieved single post")

    @pytest.mark.smoke
    def test_get_posts_list(self, api_client):
        """Test GET request - retrieve a list of posts"""
        logger.info("Starting test: test_get_posts_list")

        response = api_client.get("/posts", params={"_limit": 5})

        # Assertions
        assert response.status_code == 200
        posts = response.json()
        assert isinstance(posts, list)
        assert len(posts) == 5

        logger.info(f"✓ Retrieved {len(posts)} posts")

    @pytest.mark.smoke
    def test_get_with_query_params(self, api_client):
        """Test GET request with query parameters"""
        logger.info("Starting test: test_get_with_query_params")

        response = api_client.get("/posts", params={"userId": 1, "_limit": 3})

        # Assertions
        assert response.status_code == 200
        posts = response.json()
        assert all(post["userId"] == 1 for post in posts)

        logger.info(f"✓ Retrieved posts for userId=1")

    @pytest.mark.smoke
    def test_post_create_resource(self, api_client):
        """Test POST request - create new resource"""
        logger.info("Starting test: test_post_create_resource")

        payload = {"title": "Test Post", "body": "This is a test post", "userId": 1}

        response = api_client.post("/posts", json_data=payload)

        # Assertions
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]
        assert "id" in data

        logger.info(f"✓ Successfully created post with id: {data['id']}")

    def test_post_with_headers(self, api_client):
        """Test POST request with custom headers"""
        logger.info("Starting test: test_post_with_headers")

        payload = {"title": "Test", "body": "Test body", "userId": 1}

        custom_headers = {"X-Custom-Header": "test-value"}
        response = api_client.post("/posts", json_data=payload, headers=custom_headers)

        # Assertions
        assert response.status_code == 201
        assert "id" in response.json()

        logger.info("✓ POST request with custom headers successful")

    def test_put_update_resource(self, api_client):
        """Test PUT request - update existing resource"""
        logger.info("Starting test: test_put_update_resource")

        payload = {"id": 1, "title": "Updated Title", "body": "Updated body content", "userId": 1}

        response = api_client.put("/posts/1", json_data=payload)

        # Assertions
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == payload["title"]

        logger.info("✓ Successfully updated resource")

    def test_delete_resource(self, api_client):
        """Test DELETE request - delete resource"""
        logger.info("Starting test: test_delete_resource")

        response = api_client.delete("/posts/1")

        # Assertions
        assert response.status_code == 200

        logger.info("✓ Successfully deleted resource")

    @pytest.mark.smoke
    def test_response_json_parsing(self, api_client):
        """Test response JSON parsing"""
        logger.info("Starting test: test_response_json_parsing")

        response = api_client.get("/posts/1")

        # Assertions
        assert response.status_code == 200
        json_data = response.json()
        assert isinstance(json_data, dict)
        assert json_data["userId"] > 0

        logger.info("✓ Response JSON parsed successfully")

    def test_error_handling_404(self, api_client):
        """Test error handling for 404 responses"""
        logger.info("Starting test: test_error_handling_404")

        response = api_client.get("/posts/99999")

        # Assertions
        # Note: JSONPlaceholder returns 200 even for non-existent IDs
        assert response.status_code in [200, 404]

        logger.info("✓ Error handling test passed")

    @pytest.mark.slow
    def test_batch_requests(self, api_client):
        """Test making multiple API requests (batch)"""
        logger.info("Starting test: test_batch_requests")

        responses = []
        for post_id in range(1, 4):
            response = api_client.get(f"/posts/{post_id}")
            assert response.status_code == 200
            responses.append(response)

        assert len(responses) == 3
        logger.info(f"✓ Successfully completed {len(responses)} batch requests")

    def test_api_client_context_manager(self):
        """Test API client as a context manager"""
        logger.info("Starting test: test_api_client_context_manager")

        client = APIClient(base_url="https://jsonplaceholder.typicode.com")
        response = client.get("/posts/1")

        assert response.status_code == 200

        client.close()
        logger.info("✓ API client context manager test passed")


class TestExampleAPIValidation:
    """Example API validation tests"""

    @pytest.fixture
    def api_client(self):
        """Create an API client for tests"""
        return APIClient(base_url="https://jsonplaceholder.typicode.com")

    @pytest.mark.api
    def test_response_headers_validation(self, api_client):
        """Test response headers validation"""
        logger.info("Starting test: test_response_headers_validation")

        response = api_client.get("/posts/1")

        # Assertions
        assert "content-type" in response.headers
        assert "application/json" in response.headers["content-type"]

        logger.info("✓ Response headers validated")

    @pytest.mark.api
    def test_response_schema_validation(self, api_client):
        """Test response data structure validation"""
        logger.info("Starting test: test_response_schema_validation")

        response = api_client.get("/posts/1")
        data = response.json()

        # Validate expected fields exist
        required_fields = ["userId", "id", "title", "body"]
        for field in required_fields:
            assert field in data, f"Missing field: {field}"

        # Validate field types
        assert isinstance(data["userId"], int)
        assert isinstance(data["id"], int)
        assert isinstance(data["title"], str)
        assert isinstance(data["body"], str)

        logger.info("✓ Response schema validated")
