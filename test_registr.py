import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()


class AuthorizationFormTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://b2c.passport.rt.ru/")

    def test_display_authorization_form(self):
        authorization_form = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "page-right"))
        )
        self.assertTrue(authorization_form.is_displayed())

    def test_registration_success(self):
        self.navigate_to_registration()
        self.fill_registration_form(
            first_name=os.getenv("valid_first"),
            last_name=os.getenv("valid_last"),
            email=os.getenv("valid_email"),
            password=os.getenv("valid_password"),
            confirm_password=os.getenv("valid_password")
        )
        self.submit_registration()

    def navigate_to_registration(self):
        register_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "kc-register"))
        )
        register_button.click()

    def fill_registration_form(self, first_name, last_name, email, password, confirm_password):
        first_name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]'))
        )
        last_name_input = self.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input')
        email_input = self.driver.find_element(By.ID, "address")
        password_input = self.driver.find_element(By.ID, "password")
        confirm_password_input = self.driver.find_element(By.ID, "password-confirm")

        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        email_input.send_keys(email)
        password_input.send_keys(password)
        confirm_password_input.send_keys(password)

    def submit_registration(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/button'))
        )
        submit_button.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


#python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_registr.py