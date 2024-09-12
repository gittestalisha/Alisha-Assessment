from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class FrontendBackendIntegrationTest(unittest.TestCase):
    def setUp(self):
        # Initialize WebDriver (e.g., Chrome)
        self.driver = webdriver.Chrome()
        self.frontend_url = "http://localhost:3000"  # Replace with your frontend URL

    def test_greeting_message(self):
        driver = self.driver
        driver.get(self.frontend_url)
        
        # Optionally, if there's a button to fetch the message, click it
        # button = driver.find_element(By.ID, "fetchGreetingButton")
        # button.click()

        # Wait for the message to be displayed (modify the wait time as needed)
        driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

        # Find the element that displays the greeting message
        message_element = driver.find_element(By.ID, "greetingMessage")
        message_text = message_element.text

        # Define the expected greeting message
        expected_message = "Hello from backend!"  # Replace with the actual expected message

        # Assert that the displayed message matches the expected message
        self.assertEqual(message_text, expected_message, f"Expected message: '{expected_message}', but got: '{message_text}'")

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
