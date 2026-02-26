# Playwright Python Full Stack Demo

A comprehensive demonstration of **Playwright** with Python, showcasing both **UI automation** and **API automation** with best practices, testing frameworks, and production-ready patterns.

## 🎯 Features

- ✅ **UI Automation**: Browser automation with Playwright (Chrome, Firefox, Safari)
- ✅ **API Automation**: REST API testing with requests library
- ✅ **Page Object Model (POM)**: Scalable and maintainable test structure
- ✅ **Pytest Integration**: Comprehensive testing framework with fixtures
- ✅ **Test Parallelization**: Run tests in parallel with pytest-xdist
- ✅ **HTML Reports**: Generate beautiful test reports with pytest-html
- ✅ **CI/CD Ready**: GitHub Actions workflow included
- ✅ **Best Practices**: Environment configuration, logging, and error handling

## 📋 Project Structure

```
.
├── tests/
│   ├── ui/                          # UI automation tests
│   │   ├── test_html_page.py        # HTML page interaction tests
│   │   └── pages/                   # Page Object Models
│   │       ├── base_page.py         # Base page with common methods
│   │       └── html_page.py         # HTML page object model
│   ├── api/                         # API automation tests
│   │   ├── test_rest_api.py         # REST API test suite
│   │   └── clients/                 # API client classes
│   │       └── api_client.py        # Base API client
│   └── fixtures/
│       └── conftest.py              # Pytest configuration and fixtures
├── utils/
│   ├── __init__.py
│   ├── logger.py                    # Logging utility
│   └── helpers.py                   # Common helper functions
├── config/
│   ├── settings.py                  # Configuration management
│   └── .env.example                 # Environment variables template
├── main.py                          # Quick start example
├── pyproject.toml                   # Project configuration (uv/pip)
├── uv.lock                          # Locked dependencies (uv)
├── pytest.ini                       # Pytest configuration
├── .gitignore                       # Git ignore file
└── README.md                        # This file

```

## 🚀 Getting Started

### Prerequisites
- **Python 3.11+** (Python 3.13 recommended for best compatibility)
- uv (fast Python package manager) - Recommended
- OR pip (standard package manager)

### Installation

#### Option 1: Using UV (Recommended) ⚡

1. **Clone the repository**
```bash
git clone git@github.com:captain-nimo/plywright-demo-python-full-stack.git
cd plywright-demo-python-full-stack
```

2. **Install dependencies with UV**
```bash
uv sync
```
This automatically creates a virtual environment at `.venv/` with all dependencies.

3. **Install Playwright browsers**
```bash
uv run playwright install
```
Or if you prefer:
```bash
python -m playwright install
```

4. **Configure environment variables**
```bash
cp config/.env.example config/.env
# Edit config/.env with your settings
```

#### Option 2: Using pip

1. **Clone the repository**
```bash
git clone git@github.com:captain-nimo/plywright-demo-python-full-stack.git
cd plywright-demo-python-full-stack
```

2. **Create a virtual environment**
```bash
# If the above fails, try with --copies flag:
python3 -m venv venv --copies

# Then activate it:
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -e .
```

4. **Install Playwright browsers**
```bash
python -m playwright install
```

5. **Configure environment variables**
```bash
cp config/.env.example config/.env
# Edit config/.env with your settings
```

## 📝 Usage

### Running All Tests (with UV)
```bash
uv run pytest
# Or: uv run pytest -v
```

### Running All Tests (with activated venv)
```bash
source .venv/bin/activate
pytest
```

### Running UI Tests Only
```bash
uv run pytest tests/ui/ -v
```

### Running API Tests Only
```bash
uv run pytest tests/api/ -v
```

### Running Specific Test Markers
```bash
# Smoke tests
uv run pytest -m smoke -v

# UI tests
uv run pytest -m ui -v

# API tests
uv run pytest -m api -v

# Slow tests
uv run pytest -m slow -v
```

### Running Tests in Parallel
```bash
uv run pytest -n auto
```

### Generating HTML Report
```bash
uv run pytest --html=report.html --self-contained-html
```

### Running with Debug Mode
```bash
uv run pytest -v -s
```

### Running Specific Test
```bash
uv run pytest tests/ui/test_html_page.py::TestExampleUI::test_navigate_to_page -v
uv run pytest tests/api/test_rest_api.py::TestExampleAPI::test_get_single_post -v
```

### Quick Demo
```bash
# Run the demo script to verify setup
python main.py
```

## 🧪 Test Examples

### UI Automation Example
Tests demonstrate:
- Browser navigation
- Element interaction (click, type, select)
- Waiting for elements
- Taking screenshots
- Form submissions
- Table data extraction

### API Automation Example
Tests demonstrate:
- GET requests
- POST requests with JSON payloads
- PUT/DELETE operations
- Response validation
- Status code assertions
- JSON schema validation
- Error handling

## 🔧 Configuration

### Environment Variables
Create a `config/.env` file based on the template:
```
BASE_UI_URL=https://httpbin.org/html
API_BASE_URL=https://jsonplaceholder.typicode.com
BROWSER=chromium
HEADLESS=true
TIMEOUT=30000
```

**Note**: The default URLs point to public test APIs:
- `httpbin.org`: For UI automation testing
- `jsonplaceholder.typicode.com`: For API testing (fake JSON API)

### Pytest Configuration
Pytest settings are in `pytest.ini`:
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| playwright | 1.48.0+ | Browser automation |
| pytest | 8.3.4+ | Testing framework |
| pytest-playwright | 0.6.2+ | Pytest integration |
| requests | 2.32.3+ | HTTP API testing |
| python-dotenv | 1.0.1+ | Environment configuration |
| pytest-html | 4.1.1+ | HTML report generation |
| pytest-xdist | 3.6.1+ | Test parallelization |

## 🎓 Learning Resources

- [Playwright Python Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Requests Library Documentation](https://docs.requests.dev/)
- [Page Object Model Pattern](https://playwright.dev/python/docs/pom)

## 🔒 Security

- Never commit `.env` files with sensitive data
- Use `config/.env.example` as a template
- Store credentials in CI/CD secrets

## 📊 CI/CD Integration

This project is ready for GitHub Actions. See `.github/workflows/` for automated test execution.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Happy Testing! 🎭**

