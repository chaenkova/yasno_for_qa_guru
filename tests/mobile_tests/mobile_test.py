from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be
from datetime import date


def test_android_search_today():
    with step('Открываем поиск станций отправления'):
        browser.element((AppiumBy.ID, "ru.rzd:id/fromStationLayout")).click()
    with step('Выбираем Москву'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR,
                         'new UiSelector().text(\"Москва\")')).click()
    with step('Открываем поиск станций прибытия'):
        browser.element((AppiumBy.ID, "ru.rzd:id/toStationLayout")).click()
    with step('Выьбираем Казань'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(\"Казань\")')).click()
    with step('Открываем datapicker'):
        browser.element((AppiumBy.ID, "ru.rzd:id/dateLayout")).click()
    with step('Кликаем сегодняшнюю дату'):
        browser.element((AppiumBy.ID, "ru.rzd:id/date")).click()
    with step('Нажимаем поиск'):
        browser.element((AppiumBy.ID, "ru.rzd:id/search")).click()
    with step('На экране поезд Москва-Казань, отправление сегодня'):
        assert browser.element((AppiumBy.ID, "ru.rzd:id/toolbarStationFrom")).should(have.text('Москва'))
        assert browser.element((AppiumBy.ID, "ru.rzd:id/toolbarStationTo")).should(have.text('Казань'))

        assert browser.element((AppiumBy.ID, "ru.rzd:id/toolbarDate")).should(have.text(date.today().strftime("%d")))


def test_android_search_city():
    with step('Открываем поиск станций отправления'):
        browser.element((AppiumBy.ID, "ru.rzd:id/fromStationLayout")).click()
    with step('Вбиваем город Брянск'):
        browser.element((AppiumBy.ID, "ru.rzd:id/search")).type("Брянск")
    with step('Можно выбрать поезда на всех вокзалах города'):
        assert browser.element((AppiumBy.ID,
                                'ru.rzd:id/all_stations_bage')).should(have.text('все вокзалы'))


def test_android_search_same_city():
    with step('Открываем поиск станций отправления'):
        browser.element((AppiumBy.ID, "ru.rzd:id/fromStationLayout")).click()
    with step('Вбиваем город Брянск'):
        browser.element((AppiumBy.ID, "ru.rzd:id/search")).type("Брянск")
    with step('Есть похожие станции'):
        assert browser.element((AppiumBy.ANDROID_UIAUTOMATOR,
                                'new UiSelector().text(\"Похожие станции\")')).should(be.existing)


def test_android_clear_search_field():
    with step('Открываем поиск станций отправления'):
        browser.element((AppiumBy.ID, "ru.rzd:id/fromStationLayout")).click()
    with step('Вбиваем город Брянск'):
        browser.element((AppiumBy.ID, "ru.rzd:id/search")).type("Брянск")
    with step('Очищаем поле'):
        browser.element((AppiumBy.ID, 'ru.rzd:id/text_input_end_icon')).click()
    with step('Поле очищено'):
        assert browser.element((AppiumBy.ID, "ru.rzd:id/search")).should(have.text('Станция отправления'))


def test_android_flies():
    with step('Выбор авиабилетов'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR,
                         'new UiSelector().text(\"Самолеты\")')).click()
    with step('Текст с вопросом об авиабилетах'):
        assert browser.element((AppiumBy.ID, "ru.rzd:id/text")).should(have.text('Стоит ли нам сделать продажу авиа билетов?'))
