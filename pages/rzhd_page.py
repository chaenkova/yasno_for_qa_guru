
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be
from datetime import date
import os


class RzhdPage:

    @staticmethod
    def open_from_station():
        with step(f'Открываем поиск станций отправления'):
            browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/fromStationLayout")).click()

    @staticmethod
    def type_city(city):
        with step(f'Вбиваем город {city}'):
            browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/search")).type(f"{city}")

    @staticmethod
    def click_city(city):
        with step('Выбираем Москву'):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR,
                             f'new UiSelector().text(\"{city}\")')).click()

    @staticmethod
    def open_to_station(station):
        with step(f'Открываем поиск станций прибытия ({station})'):
            browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/toStationLayout")).click()
        with step('Выьбираем Казань'):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text(\"{station}\")')).click()

    @staticmethod
    def chose_today_date():
        with step('Открываем datapicker'):
            browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/dateLayout")).click()
        with step('Кликаем сегодняшнюю дату'):
            browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/date")).click()

    @staticmethod
    def click_search():
        with step('Нажимаем поиск'):
            browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/search")).click()

    @staticmethod
    def check_from_to_today(station_from, station_to):
        with step(f'На экране поезд {station_from}-{station_to}, отправление сегодня'):
            assert browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/toolbarStationFrom")).should(
                have.text(f'{station_from}'))
            assert browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/toolbarStationTo")).should(
                have.text(f'{station_to}'))

            assert browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/toolbarDate")).should(
                have.text(date.today().strftime("%d")))

    @staticmethod
    def check_all_station_of_city():
        with step('Можно выбрать поезда на всех вокзалах города'):
            assert browser.element((AppiumBy.ID,
                                    f"{os.getenv('APP_NAME')}/all_stations_bage")).should(have.text('все вокзалы'))

    @staticmethod
    def check_same_cities_exist():
        with step('Есть похожие станции'):
            assert browser.element((AppiumBy.ANDROID_UIAUTOMATOR,
                                    'new UiSelector().text(\"Похожие станции\")')).should(be.existing)

    @staticmethod
    def clean_field_from():
        with step('Очищаем поле'):
            browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/text_input_end_icon")).click()

    @staticmethod
    def check_clean_field():
        with step('Поле очищено'):
            assert browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/search")).should(
                have.text('Станция отправления'))

    @staticmethod
    def chose_fly():
        with step('Выбор авиабилетов'):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR,
                             'new UiSelector().text(\"Самолеты\")')).click()

    @staticmethod
    def check_fly_popup():
        with step('Текст с вопросом об авиабилетах'):
            assert browser.element((AppiumBy.ID, f"{os.getenv('APP_NAME')}/text")).should(
                have.text('Стоит ли нам сделать продажу авиа билетов?'))


rzhd = RzhdPage()
