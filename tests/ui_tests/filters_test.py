from pages.catalog_page import catalog
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.suite('Каталог')
class TestCatalogUI:
    @allure.severity(Severity.NORMAL)
    @allure.title('По-умолчанию нет выбранных фильтров')
    def test_open_catalog_without_filters(self):
        (catalog.open()
         .should_have_no_filters())

    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка работы быстрого фильтра симптомов')
    def test_symptoms_filter(self):
        (catalog.open()
         .click_close_filters_button()
         .choose_item_in_filter('Симптомы', 'Стресс')
         .click_apply_filters_button()
         .text_should_be_in_filters('Стресс'))

    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка работы быстрого фильтра подхода')
    def test_treatment_filter(self):
        (catalog.open()
         .click_close_filters_button()
         .choose_item_in_filter('Подход', 'КПТ')
         .click_apply_filters_button()
         .text_should_be_in_filters('КПТ'))

    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка работы быстрого фильтра по цене')
    def test_price_filter(self):
        (catalog.open()
         .click_close_filters_button()
         .choose_item_in_filter('Цена', '2850 ₽')
         .click_apply_filters_button()
         .text_should_be_in_filters('2850 ₽'))

    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка работы быстрого фильтра по полу')
    def test_gender_filter(self):
        (catalog.open()
         .click_close_filters_button()
         .choose_item_in_filter('Пол', 'Мужской')
         .click_apply_filters_button()
         .text_should_be_in_filters('Мужской'))

    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка работы общего фильтра по нескольким параметрам')
    def test_all_filter(self):
        (catalog.open()
         .fill_filters(catalog.filters_for_catalog_popup)
         .click_apply_filters_button('._s-popup_layer')
         .check_filters(catalog.filters_for_catalog_popup))

    @allure.severity(Severity.NORMAL)
    @allure.title('Сортировка "Сначала дороже"')
    def test_max_price_sort(self):
        (catalog.open()
         .choose_sort_max_price()
         .check_sort_max_price())

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка перехода на страницу пресета')
    def test_preset(self):
        (catalog.open()
         .fill_filters_for_preset()
         .click_apply_filters_button()
         .check_preset_title())

    @allure.severity(Severity.MINOR)
    @allure.title('Есть возможность открыть больше психологов')
    def test_see_more(self):
        (catalog.open()
         .count_therapists()
         .see_more()
         .check_count())

    @allure.severity(Severity.NORMAL)
    @allure.title('Цена в попапе грейда совпадает со стоимостью сессии')
    def test_price_popup(self):
        (catalog.open()
         .click_price_icon()
         .check_price_in_popup())

    @allure.severity(Severity.NORMAL)
    @allure.title('Выбрана парная терапия')
    def test_couple_therapy(self):
        (catalog.open()
         .choose_couple()
         .check_couple())
