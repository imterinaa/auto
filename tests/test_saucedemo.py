from pages.SauceDemoPage import SauceDemoPage

def test_pom(browser):
    page = SauceDemoPage(browser)
    browser.get("https://www.saucedemo.com/")
    
    page.login("standard_user", "secret_sauce")
    page.add_to_cart("sauce-labs-backpack")
    assert page.get_cart_count() == "1"
