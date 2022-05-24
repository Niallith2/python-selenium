from selenium.webdriver.common.by import By


def test_button_buscket_is_present(browser):
    browser.get("http://selenium1py.pythonanywhere.com/")
    assert browser.find_element(By.CSS_SELECTOR, "span.btn-group > a").is_displayed()
