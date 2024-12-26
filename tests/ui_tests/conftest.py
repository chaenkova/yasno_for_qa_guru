import pytest
from selene import browser
from helpers import attaches
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function", autouse=True)
def browser_settings():
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = os.getenv("BASE_URL")
    browser.config.timeout = 3

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options)

    browser.config.driver = driver

    yield
    attaches.add_html(browser)
    attaches.add_screenshot(browser)
    attaches.add_logs(browser)
    attaches.add_video(browser)
    browser.quit()
