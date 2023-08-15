import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()


class PasswordRecoveryTypeSelectionTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://b2c.passport.rt.ru/")

    def test_password_recovery_type_selection(self):
        # Wait for the page to load and the element to become clickable
        recovery_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "forgot_password"))
        )
        recovery_link.click()

        recovery_type_window = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "page-right"))
        )
        self.assertTrue(recovery_type_window.is_displayed())

        phone_input = self.driver.find_element(By.XPATH, '//*[@id="username"]')
        continue_button = self.driver.find_element(By.ID, "reset")

        phone_number = os.getenv("valid_phone")
        phone_input.send_keys(phone_number)
        continue_button.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

#python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_forgot_pass.py