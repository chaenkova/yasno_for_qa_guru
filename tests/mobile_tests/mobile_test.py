import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be
from datetime import date
import os


def test_android_search_today():
    with step('Открываем поиск станций отправления'):
        browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/fromStationLayout")).click()
    with step('Выбираем Москву'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR,
                         'new UiSelector().text(\"Москва\")')).click()
    with step('Открываем поиск станций прибытия'):
        browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/toStationLayout")).click()
    with step('Выьбираем Казань'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(\"Казань\")')).click()
    with step('Открываем datapicker'):
        browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/dateLayout")).click()
    with step('Кликаем сегодняшнюю дату'):
        browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/date")).click()
    with step('Нажимаем поиск'):
        browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/search")).click()
    with step('На экране поезд Москва-Казань, отправление сегодня'):
        assert browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/toolbarStationFrom")).should(have.text('Москва'))
        assert browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/toolbarStationTo")).should(have.text('Казань'))

        assert browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/toolbarDate")).should(
            have.text(date.today().strftime("%d")))


@pytest.mark.parametrize("city", ['Брянск', 'Казань', 'Неверленд'])
def test_android_rzhd_search_terminal(city):
    with step('Открываем поиск станций отправления'):
        browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/fromStationLayout")).click()
    with step('Вбиваем город Брянск'):
        browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/search")).type("Брянск")
    with step('Можно выбрать поезда на всех вокзалах города'):
        assert browser.element((AppiumBy.ID,
                                f"{os.getenv('APP_NAME')}/all_stations_bage")).should(have.text('все вокзалы'))


@pytest.mark.parametrize("city", ['Брянск'])
def test_android_rzhd_search_city_duplicates(city):
    with step('Открываем поиск станций отправления'):
        browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/fromStationLayout")).click()
    with step('Вбиваем город'):
        browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/search")).type(city)
    with step('Есть похожие станции'):
        assert browser.element((AppiumBy.ANDROID_UIAUTOMATOR,
                                'new UiSelector().text(\"Похожие станции\")')).should(be.existing)


def test_android_rzhd_clear_search_field():
    with step('Открываем поиск станций отправления'):
        browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/fromStationLayout")).click()
    with step('Вбиваем город Брянск'):
        browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/search")).type("Брянск")
    with step('Очищаем поле'):
        browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/text_input_end_icon")).click()
    with step('Поле очищено'):
        assert browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/search")).should(
            have.text('Станция отправления'))


def test_android_flies_waiting_text_is_present():
    with step('Выбор авиабилетов'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR,
                         'new UiSelector().text(\"Самолеты\")')).click()
    with step('Текст с вопросом об авиабилетах'):
        assert browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/text")).should(
            have.text('Стоит ли нам сделать продажу авиа билетов?'))
