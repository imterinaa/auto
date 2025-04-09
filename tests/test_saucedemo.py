import allure
from pages.SauceDemoPage import SauceDemoPage

@allure.epic("SauceDemo Tests")
@allure.feature("Корзина покупок")
@allure.story("Добавление товара в корзину")
def test_pom(browser):
    """Тест добавления товара в корзину с использованием Page Object Model"""
    
    page = SauceDemoPage(browser)
    
    with allure.step("1. Открыть главную страницу"):
        browser.get("https://www.saucedemo.com/")
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Main Page",
            attachment_type=allure.attachment_type.PNG
        )
    
    with allure.step("2. Выполнить авторизацию"):
        page.login("standard_user", "secret_sauce")
        allure.attach(
            browser.get_screenshot_as_png(),
            name="After Login",
            attachment_type=allure.attachment_type.PNG
        )
    
    with allure.step("3. Добавить товар в корзину"):
        page.add_to_cart("sauce-labs-backpack")
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Item Added",
            attachment_type=allure.attachment_type.PNG
        )
    
    with allure.step("4. Проверить счетчик корзины"):
        cart_count = page.get_cart_count()
        allure.attach(
            f"Текущее значение счетчика: {cart_count}",
            name="Cart Counter",
            attachment_type=allure.attachment_type.TEXT
        )
        assert cart_count == "1", "Счетчик корзины должен показывать 1 товар"
