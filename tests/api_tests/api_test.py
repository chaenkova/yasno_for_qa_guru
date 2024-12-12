from helpers.request import send_request
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.suite('api для каталога')
class TestCatalogAPI:
    stress_preset_ids = {"question_ids": [1, 2]}
    stress_preset_name = "Стресс"

    stress_preset_id = {
        "search_preset_id": 16
    }
    stress_preset_url = {
        "url_slug": "stress"
    }

    @allure.severity(Severity.NORMAL)
    @allure.title('При подсчете психологов приходит валидный ответ ')
    def test_api_psychologist_count(self):
        response = send_request("catalog/count", 'post', self.stress_preset_ids)

        allure.step(f'Проверям статус ответа от сервера')
        assert response.status_code == 200

    @allure.severity(Severity.NORMAL)
    @allure.title('Валидный ответ при получении списка пресетов')
    def test_api_get_presets(self):
        response = send_request("catalog/search_presets", 'get')

        allure.step(f'Проверям статус ответа от сервера')
        assert response.status_code == 200

    @allure.severity(Severity.NORMAL)
    @allure.title('Валидный ответ при получении пресета по id')
    def test_api_get_by_presets(self):
        response = send_request("catalog/by_search_preset", 'post', self.stress_preset_id).json()

        assert response["data"]["search_preset"]["short_title"] == TestCatalogAPI.stress_preset_name

    @allure.severity(Severity.NORMAL)
    @allure.title('Валидный ответ при получении конкретного пресета')
    def test_api_get_preset(self):
        response = send_request("catalog/search_preset", 'post', self.stress_preset_url).json()

        assert response["data"]["search_preset"]["short_title"] == TestCatalogAPI.stress_preset_name

    @allure.severity(Severity.NORMAL)
    @allure.title('Валидный ответ при получении страницы каталога')
    def test_api_get_catalog(self):
        response = send_request("catalog", 'post', self.stress_preset_ids).json()

        print(response)

        assert response['data']['search_preset']['short_title'] == 'Все психологи'
