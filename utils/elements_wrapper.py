import time
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

class ElementWrapper:
    """
    Wrapper class for Playwright elements to handle exceptions and provide
    reusable methods for interacting with elements.
    """
    
    def __init__(self, page: Page, locator: str, timeout: int = 30000):
        self.page = page
        self.locator = locator
        self.timeout = timeout
        
    def _get_element(self, timeout=5000):
        """
        Get the element with specified locator.
        
        Args:
            timeout (int): Timeout in milliseconds (default: 5000)
        
        Returns:
            The Playwright locator object.
        """
        # Handle different locator types
        if isinstance(self.locator, tuple):
            locator_type, locator_value = self.locator
            
            if locator_type == "css":
                return self.page.locator(locator_value)
            elif locator_type == "xpath":
                return self.page.locator(f"xpath={locator_value}")
            elif locator_type == "text":
                return self.page.get_by_text(locator_value)
            elif locator_type == "role":
                return self.page.get_by_role(locator_value)
            elif locator_type == "test_id":
                return self.page.get_by_test_id(locator_value)
            elif locator_type == "placeholder":
                return self.page.get_by_placeholder(locator_value)
            elif locator_type == "alt_text":
                return self.page.get_by_alt_text(locator_value)
            elif locator_type == "label":
                return self.page.get_by_label(locator_value)
            elif locator_type == "title":
                return self.page.get_by_title(locator_value)
            else:
                raise ValueError(f"Unsupported locator type: {locator_type}")
        
        # If it's a string, treat it as CSS selector by default
        elif isinstance(self.locator, str):
            # Check if the string already starts with a specific locator type
            if self.locator.startswith(("xpath=", "text=", "id=", "css=")):
                return self.page.locator(self.locator)
            # Default to CSS selector
            return self.page.locator(self.locator)
        
        else:
            raise TypeError(f"Locator must be a string or tuple, got {type(self.locator)}")
    
    def is_visible(self, timeout: int = None) -> bool:
        """Check if element is visible"""
        timeout = timeout or self.timeout
        try:
            return self._get_element().is_visible(timeout=timeout)
        except PlaywrightTimeoutError:
            return False
        except Exception as e:
            print(f"Error checking visibility for {self.locator}: {str(e)}")
            return False
    
    def click(self, force: bool = False, timeout: int = None) -> bool:
        """Click on the element"""
        timeout = timeout or self.timeout
        try:
            self._get_element().click(force=force, timeout=timeout)
            return True
        except Exception as e:
            print(f"Error clicking on {self.locator}: {str(e)}")
            return False
    
    def fill(self, text: str, timeout: int = None) -> bool:
        """Fill text in the element"""
        timeout = timeout or self.timeout
        try:
            self._get_element().fill(text, timeout=timeout)
            return True
        except Exception as e:
            print(f"Error filling text in {self.locator}: {str(e)}")
            return False
    
    def get_text(self, timeout: int = None) -> str:
        """Get text of the element"""
        timeout = timeout or self.timeout
        try:
            return self._get_element().text_content(timeout=timeout)
        except Exception as e:
            print(f"Error getting text from {self.locator}: {str(e)}")
            return ""
    
    def wait_for_visibility(self, timeout: int = None) -> bool:
        """Wait for element to be visible"""
        timeout = timeout or self.timeout
        try:
            self._get_element().wait_for(state="visible", timeout=timeout)
            return True
        except Exception as e:
            print(f"Error waiting for visibility of {self.locator}: {str(e)}")
            return False
    
    def wait_for_element(self, timeout: int = None) -> bool:
        """Wait for element to exist in DOM"""
        timeout = timeout or self.timeout
        try:
            self._get_element().wait_for(timeout=timeout)
            return True
        except Exception as e:
            print(f"Error waiting for element {self.locator}: {str(e)}")
            return False
    
    def select_option(self, value: str, timeout: int = None) -> bool:
        """Select an option from dropdown by value"""
        timeout = timeout or self.timeout
        try:
            self._get_element().select_option(value=value, timeout=timeout)
            return True
        except Exception as e:
            print(f"Error selecting option in {self.locator}: {str(e)}")
            return False
    
    def check(self, timeout: int = None) -> bool:
        """Check a checkbox or radio button"""
        timeout = timeout or self.timeout
        try:
            self._get_element().check(timeout=timeout)
            return True
        except Exception as e:
            print(f"Error checking {self.locator}: {str(e)}")
            return False
