from helpers.request import send_request, check_response_code
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
    @allure.title('При подсчете психологов приходит больше 0 ')
    def test_api_psychologist_count(self):
        response = send_request("catalog/count", 'post', self.stress_preset_ids)

        assert response.json()["data"]["count"] > 0

        check_response_code(response, 200)

    @allure.severity(Severity.NORMAL)
    @allure.title('Валидный ответ при получении списка пресетов')
    def test_api_get_presets(self):
        response = send_request("catalog/search_presets", 'get')

        assert len(response.json()["data"]["search_presets"]) > 0
        check_response_code(response, 200)

    @allure.severity(Severity.NORMAL)
    @allure.title('Валидный ответ при получении пресета по id')
    def test_api_get_by_presets(self):
        response = send_request("catalog/by_search_preset", 'post', self.stress_preset_id)

        assert response.json()["data"]["search_preset"]["short_title"] == TestCatalogAPI.stress_preset_name
        check_response_code(response, 200)

    @allure.severity(Severity.NORMAL)
    @allure.title('Валидный ответ при получении конкретного пресета')
    def test_api_get_preset(self):
        response = send_request("catalog/search_preset", 'post', self.stress_preset_url)

        assert response.json()["data"]["search_preset"]["short_title"] == TestCatalogAPI.stress_preset_name
        check_response_code(response, 200)

    @allure.severity(Severity.NORMAL)
    @allure.title('Валидный ответ при получении страницы каталога')
    def test_api_get_catalog(self):
        response = send_request("catalog", 'post', self.stress_preset_ids)
        check_response_code(response, 200)

        assert response.json()['data']['search_preset']['short_title'] == 'Все психологи'

