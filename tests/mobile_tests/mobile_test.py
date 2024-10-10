from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_android_search_stations():
    with step('Открываем поиск станций отправления'):
        browser.element((AppiumBy.ID, "ru.rzd:id/fromStationLayout")).click()


def test_ios_max_price_sort():
    pass
