from pages.auth_page import auth_page
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.suite('api для авторизации')
@allure.title('Авторизация')
def test_api_auth():
    pass


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.suite('api для авторизации')
@allure.title('Выход из аккаунта')
def test_api_logout():
    pass
