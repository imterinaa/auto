import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@allure.feature("Saucedemo Tests")
class TestSaucedemo:
    @allure.story("Успешная авторизация")
    def test_login(self, driver):
        with allure.step("Открываем страницу авторизации"):
            driver.get("https://www.saucedemo.com/")

        with allure.step("Вводим логин и пароль"):
            username = driver.find_element(By.ID, "user-name")
            password = driver.find_element(By.ID, "password")
            login_button = driver.find_element(By.ID, "login-button")

            username.send_keys("standard_user")
            password.send_keys("secret_sauce")
            login_button.click()

        with allure.step("Проверяем успешный вход"):
            WebDriverWait(driver, 10).until(
                EC.url_contains("/inventory.html")
            )
            assert "inventory" in driver.current_url
