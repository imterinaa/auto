import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import allure

@allure.feature("DemoQA")
def test_text_box():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)

    with allure.step("Открываем страницу"):
        driver.get("https://demoqa.com/text-box")

    with allure.step("Заполняем форму"):
        driver.find_element(By.ID, "userName").send_keys("Test User")
        driver.find_element(By.ID, "userEmail").send_keys("test@example.com")
        driver.find_element(By.ID, "currentAddress").send_keys("Some address")
        driver.find_element(By.ID, "submit").click()

    with allure.step("Проверяем результат"):
        output = driver.find_element(By.ID, "output").text
        assert "Test User" in output

    driver.quit()
  
