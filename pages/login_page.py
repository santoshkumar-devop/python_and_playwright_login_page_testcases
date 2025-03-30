from time import sleep
from utils.base_page import BasePage

class LoginPage(BasePage):
    """Page Object Model for the Login Page"""
    
    # Element locators
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    SIGNIN_BUTTON = "#signInBtn"
    ERROR_MESSAGE = ".alert-danger"
    USER_DROPDOWN = "select.form-control"
    TERMS_CHECKBOX = "#terms"
    RADIO_USER = ".radiotextsty"
    BLINKING_TEXT = ".blinkingText"
    
    def __init__(self, page, config_path: str = "./config/config.json"):
        super().__init__(page, config_path)
        self.username_input = self.create_element(self.USERNAME_INPUT)
        self.password_input = self.create_element(self.PASSWORD_INPUT)
        self.signin_button = self.create_element(self.SIGNIN_BUTTON)
        self.error_message = self.create_element(self.ERROR_MESSAGE)
        self.user_dropdown = self.create_element(self.USER_DROPDOWN)
        self.terms_checkbox = self.create_element(self.TERMS_CHECKBOX)
        self.blinking_text = self.create_element(self.BLINKING_TEXT)
    
    def navigate(self) -> bool:
        """Navigate to login page"""
        return self.navigate_to()
    
    def login(self, username: str, password: str) -> bool:
        """Login with the specified credentials"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.signin_button.click()
    
    def get_error_message(self) -> str:
        """Get error message if login fails"""
        return self.error_message.get_text()
    
    def select_user_type(self, user_type: str) -> bool:
        """Select user type from dropdown"""
        return self.user_dropdown.select_option(user_type)
    
    def accept_terms(self) -> bool:
        """Check the terms and conditions checkbox"""
        return self.terms_checkbox.check()
    
    def is_signed_in(self) -> bool:
        """Check if user is signed in by verifying URL change"""
        try:
           # Wait for the URL to change to the expected path
            self.page.wait_for_url("**/angularpractice/shop", timeout=10000)  # Adjust timeout as needed
            current_url = self.page.url
            return "angularpractice/shop" in current_url
        except Exception as e:
            print(f"Error checking if signed in: {str(e)}")
            return False