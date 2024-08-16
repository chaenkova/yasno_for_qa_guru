from pages.catalog_page import catalog
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.suite('Каталог')
@allure.title('Открыта страница каталога терапевтов')
def test_open_catalog_without_filters():
    catalog.open().should_have_no_filters()


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.suite('Каталог')
@allure.title('Проверка работы быстрого фильтра симптомов')
def test_symptoms_filter():
    catalog.open().chose_stress().text_should_be_in_filters('Стресс')


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.suite('Каталог')
@allure.title('Проверка работы быстрого фильтра подхода')
def test_treatment_filter():
    catalog.open().chose_kpt().text_should_be_in_filters('КПТ')


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.suite('Каталог')
@allure.title('Проверка работы быстрого фильтра по цене')
def test_price_filter():
    catalog.open().chose_price().text_should_be_in_filters('2850 ₽')


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.suite('Каталог')
@allure.title('Проверка работы быстрого фильтра по полу')
def test_sex_filter():
    catalog.open().chose_sex().text_should_be_in_filters('Мужской')


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.suite('Каталог')
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
