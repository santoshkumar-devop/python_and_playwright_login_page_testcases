Python and Playwright Login Page Testcases



This is a Playwright-based **Test Automation Framework** designed to validate the **login** functionality of a web application. The framework is built using the Page Object Model (POM) design pattern, ensuring modularity, scalability, and ease of maintenance. It supports cross-browser testing, configurable settings, and generates detailed HTML reports for test execution results.

The framework includes:

1. **Test Data Management**: Test data is stored in JSON format (data/test_data.json) for easy configuration and scalability.
2. **Reusable Components:** Utility classes like BasePage and ElementWrapper provide reusable methods for interacting with web elements.
3. **Configurable Settings:** Configuration is managed via a JSON file (config/config.json) to allow flexibility in setting base URLs, paths, and browser options.
4. **Cross-Browser Support:** Tests can run on Chromium, Firefox, and WebKit browsers using Playwright's capabilities.
5. **Reporting**: Test results are generated in HTML format (reports/test_report.html) for easy analysis.
6. **Error Handling**: Robust error handling and screenshot capture for failed test cases ensure better debugging and traceability.

To Execute the Testcases, Follow the below steps
1. Clone the repo
    - git clone https://github.com/santoshkumar-devop/python_and_playwright_login_page_testcases.git
2. Install the libraries from requirements.txt
     - pip install -r requiremenets.txt
3. Execute the testcases
     -  pytest --html=report.html
   
