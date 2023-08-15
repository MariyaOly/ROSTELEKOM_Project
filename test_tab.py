

#python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_tab.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TabOrderTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://b2c.passport.rt.ru/")

    def test_tab_order(self):
        # Wait for the tab buttons to be clickable
        phone_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="phone_auth_tab"]'))
        )
        email_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="email_auth_tab"]'))
        )
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="standard_auth_tab"]'))
        )
        account_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="account_auth_tab"]'))
        )

        # Simulate tab navigation
        buttons = [phone_button, email_button, login_button, account_button]

        for button in buttons:
            button.send_keys(Keys.TAB)

            # You can add assertions here to verify the tab order

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
