import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
load_dotenv()


class AuthorizationFormTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://b2c.passport.rt.ru/")

    def test_display_authorization_form(self):
        # Verify that the "Authorization" form is displayed
        authorization_form = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "page-right"))
        )
        self.assertTrue(authorization_form.is_displayed())

    def test_email_auth_success(self):
        # Click the email authentication tab
        email_auth_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "t-btn-tab-mail"))
        )
        email_auth_button.click()
        email_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID,"username"))
        )
        email_input.send_keys(os.getenv("valid_email"))
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "password"))
        )
        password_input.send_keys(os.getenv("valid_password"))
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "kc-login"))
        )
        submit_button.click()

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()


#python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_authorization.py