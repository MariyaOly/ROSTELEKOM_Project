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


    def test_phone_auth_incorrect_data(self):
        phone_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "kc-login"))
        )
        phone_input.send_keys(os.getenv("invalid_phone"))
        submit_button.click()
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        phone_input.clear()
        password_input.send_keys(os.getenv("valid_password"))
        submit_button.click()

#python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_phone.py

