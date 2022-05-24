import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


languages = ["es", "fr", "en"]


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None)


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    language = request.config.getoption("language")

    if language in languages:
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
    else:
        options.add_experimental_option('prefs', {'intl.accept_languages': "ru"})

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()