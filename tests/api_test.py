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


