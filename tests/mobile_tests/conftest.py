import pytest
from selene import browser, support
from helpers import attaches
from selenium import webdriver
import allure
import allure_commons
from dotenv import load_dotenv
import os
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

import config

from appium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--device_name',
        default='Google Pixel 3'
    )
    parser.addoption(
        "--iosonly",
        required=False,
        default='false'
    )
    parser.addoption(
        "--androidonly",
        required=False,
        default='false'
    )
    parser.addoption(
        "--context",
        required=False,
        default='bstack'
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def pytest_collection_modifyitems(config, items: list[pytest.Item]):
    items.sort(key=lambda x: x.name, reverse=True)

    for item in items:
        if ("ios" not in item.name) and (config.getoption("--iosonly").lower() == "true"):
            item.add_marker(pytest.mark.skip("Мы запустили только ios тесты"))
        elif "android" not in item.name:
            item.add_marker(pytest.mark.skip("Мы запустили только android тесты"))


@pytest.fixture(scope="function", autouse=True)
def browser_settings(request):

    device_name = request.config.getoption('--device_name')
    context = request.config.getoption('--context')

    print(context)

    capabilities = config.to_driver_options(context=context, device_name=device_name)

    if context == 'bstack':
        if request.config.getoption('--androidonly').lower() == "true":
            options = UiAutomator2Options().load_capabilities(capabilities).set_capability('app', os.getenv('app'))
        elif request.config.getoption('--iosonly').lower() == "true":
            options = XCUITestOptions().load_capabilities(capabilities).set_capability('app', 'bs://sample.app')
        else:
            print('unknown device')
    else:
        options = capabilities

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )
    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)

    yield

    if context == 'bstack':
        attaches.add_screenshot(browser)
        # attaches.attach_xml(browser)
        session_id = browser.config.driver.session_id

        with allure.step('tear down app session'):
            browser.quit()

        attaches.attach_bstack_video(session_id)
