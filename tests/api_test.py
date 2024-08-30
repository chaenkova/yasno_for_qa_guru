from helpers.request import send_request
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.suite('api для каталога')
@allure.title('Корректность работы подсчета терапевтов')
def test_api_psychologist_count():
    data_request = {"question_ids": [1, 2]}
    send_request("catalog/count", 'post', data_request)


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.suite('api для каталога')
@allure.title('Получение списка пресетов')
def test_api_get_presets():
    send_request("catalog/search_presets", 'get')


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.suite('api для каталога')
@allure.title('Получение пресета по id')
def test_api_get_by_presets():
    data = {
        "search_preset_id": 16
    }
    response = send_request("catalog/by_search_preset", 'post', data).json()
    assert response["data"]["search_preset"]["short_title"] == "Стресс"


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.suite('api для каталога')
@allure.title('Получение конкретного пресета')
def test_api_get_preset():
    data = {
        "url_slug": "stress"
    }
    response = send_request("catalog/search_preset", 'post', data).json()

    assert response["data"]["search_preset"]["short_title"] == "Стресс"


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.suite('api для каталога')
@allure.title('Получение страницы каталога')
def test_api_get_catalog():
    data_request = {"question_ids": [1, 2]}
    response = send_request("catalog", 'post', data_request).json()

    assert response['data']['search_preset']['short_title'] == 'Все психологи'
