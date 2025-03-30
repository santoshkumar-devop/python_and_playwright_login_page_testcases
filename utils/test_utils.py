import json
import os

class TestUtils:
    """Utility class for test functions"""
    
    @staticmethod
    def load_test_data(file_path: str) -> dict:
        """Load test data from JSON file"""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading test data from {file_path}: {str(e)}")
    
    @staticmethod
    def create_screenshot_dir(dir_path: str) -> bool:
        """Create screenshot directory if it doesn't exist"""
        try:
            os.makedirs(dir_path, exist_ok=True)
            return True
        except Exception as e:
            print(f"Error creating directory {dir_path}: {str(e)}")
            return False