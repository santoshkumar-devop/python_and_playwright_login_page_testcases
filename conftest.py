import json
import datetime
import pytest
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    """Add browser option to pytest command line arguments"""
    parser.addoption(
        "--browser-type", 
        action="store", 
        default="chromium", 
        help="Browser to run tests on: chromium, firefox, or webkit"
    )

@pytest.fixture(scope="session")
def config():
    """Load configuration from config file"""
    try:
        with open("./config/config.json", "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading configuration: {str(e)}")

@pytest.fixture(scope="session")
def browser_type(request):
    """Get browser type from command line option"""
    return request.config.getoption("--browser-type")

@pytest.fixture(scope="session")
def browser(browser_type, config):
    """Browser fixture that runs based on specified browser type"""
    browser_config = config.get("browsers", {}).get(browser_type, {})
    headless = browser_config.get("headless", False)
    
    with sync_playwright() as playwright:
        if browser_type == "chromium":
            browser_instance = playwright.chromium.launch(headless=headless)
        elif browser_type == "firefox":
            browser_instance = playwright.firefox.launch(headless=headless)
        elif browser_type == "webkit":
            browser_instance = playwright.webkit.launch(headless=headless)
        else:
            print(f"Unsupported browser '{browser_type}', defaulting to chromium")
            browser_instance = playwright.chromium.launch(headless=headless)
            
        yield browser_instance
        browser_instance.close()

@pytest.fixture
def page(browser):
    """Get page fixture"""
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()

@pytest.fixture
def test_data(config):
    """Load test data from JSON file"""
    from utils.test_utils import TestUtils
    return TestUtils.load_test_data(config.get("test_data_path", "./data/test_data.json"))

@pytest.fixture(scope="function")
def context_with_video(request, browser):
    """Fixture to create a browser context with video recording named after the test case."""
    suite_name = "login_test_suite"
    test_name = request.node.name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    video_dir = f"videos/{suite_name}_{test_name}_{timestamp}/"
    
    context = browser.new_context(record_video_dir=video_dir)
    yield context
    context.close()