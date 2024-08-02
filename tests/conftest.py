import pytest
from selene import browser
from helpers import attaches
from selenium import webdriver
from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def browser_settings():
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://yasno.live'

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

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
