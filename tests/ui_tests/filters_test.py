import pytest

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

    @pytest.mark.parametrize("filters, value",
                             [('Симптомы', 'Стресс'), ('Подход', 'КПТ'), ('Цена', '2850 ₽'), ('Пол', 'Мужской')])
    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка работы быстрого фильтра')
    def test_fast_filters(self, filters, value):
        catalog.open() \
            .click_close_filters_button(locator=catalog.popup) \
            .choose_item_in_filter(filters, value) \
            .click_apply_filters_button(catalog.short_filter_select) \
            .text_should_be_in_filters(value)

    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка работы общего фильтра по нескольким параметрам')
    def test_all_filters(self):
        catalog.open() \
            .fill_filters(catalog.filters_for_catalog_popup) \
            .click_apply_filters_button(catalog.popup) \
            .check_filters(catalog.filters_for_catalog_popup)

    @allure.severity(Severity.NORMAL)
    @allure.title('Сортировка "Сначала дороже"')
    def test_max_price_sort(self):
        catalog.open()\
         .choose_sort_max_price()\
         .check_sort_max_price()

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка перехода на страницу пресета')
    def test_preset(self):
        catalog.open() \
            .fill_filters_for_preset() \
            .click_apply_filters_button(locator=catalog.popup) \
            .check_preset_title()

    @allure.severity(Severity.MINOR)
    @allure.title('Есть возможность открыть больше психологов')
    def test_see_more(self):
        catalog.open() \
            .count_therapists() \
            .see_more() \
            .check_count()

    @allure.severity(Severity.NORMAL)
    @allure.title('Цена в попапе грейда совпадает со стоимостью сессии')
    def test_price_popup(self):
        catalog.open() \
            .click_price_icon() \
            .check_price_in_popup()

    @allure.severity(Severity.NORMAL)
    @allure.title('Выбрана парная терапия')
    def test_couple_therapy(self):
        catalog.open() \
            .choose_couple() \
            .check_couple_symptoms_in_popup() \
            .click_apply_filters_button(locator=catalog.popup) \
            .check_couple()
