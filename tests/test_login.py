import pytest
import datetime
from pages.login_page import LoginPage


class TestLogin:
    """Test class for login functionality"""

    @pytest.mark.parametrize("credentials", ["valid_credentials"])
    def test_valid_login(self, context_with_video, test_data, credentials):
        """Test login with valid credentials"""
        page = context_with_video.new_page()
        login_page = LoginPage(page)
        
        # Navigate to the login page
        assert login_page.navigate(), "Failed to navigate to login page"
        
        # Loop through all valid credentials
        for cred in test_data.get(credentials, []):
            username = cred.get("username")
            password = cred.get("password")
            
            # Perform login
            login_page.login(username, password)
            # Check if login was successful
            if login_page.is_signed_in():
                # Take success screenshot
                login_page.take_screenshot(f"success_login_{username}")
                assert True, f"Successfully logged in with {username}/{password}"
            else:
                # Take failure screenshot
                login_page.take_screenshot(f"failed_valid_login_{username}")
                assert False, f"Login failed with valid credentials {username}/{password}"

    @pytest.mark.parametrize("credentials", ["invalid_credentials"])
    def test_invalid_login(self, context_with_video, test_data, credentials, config):
        """Test login with invalid credentials"""
        page = context_with_video.new_page()
        login_page = LoginPage(page)
        
        # Navigate to the login page
        assert login_page.navigate(), "Failed to navigate to login page"
        
        # Loop through all invalid credentials
        for cred in test_data.get(credentials, []):
            username = cred.get("username")
            password = cred.get("password")
            expected_error = cred.get("error_message")
            
            # Perform login
            login_page.login(username, password)
            
            # Check if error message is displayed
            actual_error = login_page.get_error_message()
            
            # Take screenshot regardless of result for evidence
            screenshot_path = login_page.take_screenshot(f"invalid_login_{username}")
            
            # Assert error message is as expected
            if expected_error in actual_error:
                assert True, f"Error message matched for invalid login: {actual_error}"
            else:
                assert False, f"Expected error '{expected_error}' but got '{actual_error}'"