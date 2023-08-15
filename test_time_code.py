import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class LoginWithTempCodeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://start.rt.ru/")


    def test_login_with_temp_code(self):
        temp_code_button = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "back_to_otp_btn"))
        )
        temp_code_button.click()

        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "address"))
        )
        email_input.send_keys(os.getenv("valid_email"))

        # Click the "Get Code" button
        get_code_button = self.driver.find_element(By.ID, "otp_get_code")
        get_code_button.click()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


#python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_time_code.py
