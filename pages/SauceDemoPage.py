from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceDemoPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def add_to_cart(self, item_id):
        self.driver.find_element(By.ID, f"add-to-cart-{item_id}").click()

    def get_cart_count(self):
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
