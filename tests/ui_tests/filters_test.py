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
    catalog.open().fill_filters().check_filters()


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.suite('Каталог')
@allure.title('Сортировка "Сначала дороже"')
def test_max_price_sort():
    catalog.open().chose_sort_max_price().check_sort_max_price()


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.suite('Каталог')
@allure.title('Проверка перехода на страницу пресета')
def test_preset():
    catalog.open().fill_filters_for_preset().check_preset_title()


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.suite('Каталог')
@allure.title('Есть возможность открыть больше психологов')
def test_see_more():
    catalog.open().count_therapists().see_more().check_count()


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.suite('Каталог')
@allure.title('Цена в попапе грейда совпадает со стоимостью сессии')
def test_price_popup():
    catalog.open().click_price_icon().check_price_in_popup()


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.suite('Каталог')
@allure.title('Выбрана парная терапия')
def test_couple_therapy():
    catalog.open().chose_couple().check_couple()
