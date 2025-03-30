import json
import os
from playwright.sync_api import Page
from utils.elements_wrapper import ElementWrapper

class BasePage:
    """
    Base page class that all page models inherit from.
    Contains common methods and properties.
    """
    
    def __init__(self, page: Page, config_path: str = "../config/config.json"):
        self.page = page
        self.config = self._load_config(config_path)
        
    def _load_config(self, config_path: str) -> dict:
        """Load configuration from JSON file"""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config from {config_path}: {str(e)}")
    
    def navigate_to(self, url: str = None) -> bool:
        """Navigate to URL"""
        try:
            target_url = url or self.config.get("base_url")
            self.page.goto(target_url)
            return True
        except Exception as e:
            print(f"Error navigating to {url}: {str(e)}")
            return False
    
    def get_title(self) -> str:
        """Get page title"""
        try:
            return self.page.title()
        except Exception as e:
            print(f"Error getting page title: {str(e)}")
            return ""
    
    def take_screenshot(self, name: str) -> str:
        """Take screenshot and save it to the specified path"""
        try:
            screenshot_path = self.config.get("screenshot_path", "./screenshots")
            os.makedirs(screenshot_path, exist_ok=True)
            path = os.path.join(screenshot_path, f"{name}_{self._get_timestamp()}.png")
            self.page.screenshot(path=path)
            return path
        except Exception as e:
            print(f"Error taking screenshot: {str(e)}")
            return ""
    
    def _get_timestamp(self) -> str:
        """Get current timestamp for screenshot name"""
        import datetime
        return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def create_element(self, locator: str) -> ElementWrapper:
        """Create an ElementWrapper instance for the given locator"""
        return ElementWrapper(
            self.page, 
            locator, 
            self.config.get("timeout", 30000)
        )