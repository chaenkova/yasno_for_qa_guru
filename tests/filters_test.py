from pages.catalog_page import CatalogPage
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.suite('Каталог')
@allure.title('Открыта страница каталога терапевтов')
def test_open_catalog_without_filters():
    catalog = CatalogPage()
    catalog.open().should_have_no_filters()


@allure.title('Проверка работы быстрого фильтра симптомов')
def test_symptoms_filter():
    catalog = CatalogPage()
    catalog.open().chose_stress().text_should_be_in_filters('Стресс')


@allure.title('Проверка работы быстрого фильтра подхода')
def test_treatment_filter():
    catalog = CatalogPage()
    catalog.open().chose_kpt().text_should_be_in_filters('КПТ')


@allure.title('Проверка работы быстрого фильтра по цене')
def test_price_filter():
    catalog = CatalogPage()
    catalog.open().chose_price().text_should_be_in_filters('2850 ₽')

@allure.title('Проверка работы быстрого фильтра по полу')
def test_sex_filter():
    catalog = CatalogPage()
    catalog.open().chose_sex().text_should_be_in_filters('Мужской')


@allure.title('Проверка работы общего фильтра по нескольким параметрам')
def test_all_filter():
    pass


def test_max_price_sort():
    pass


def test_preset():
    pass


def test_see_more():
    pass


def test_api_pycholog_rate():
    pass


def test_education_popup():
    pass


def test_couple_therapy():
    pass
