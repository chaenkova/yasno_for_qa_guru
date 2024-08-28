import json
import allure
from helpers.attaches import request_with_logs
from jsonschema import validate
from pathlib import Path


def send_request(endpoint, method, data):
    allure.step(f'Делаем запрос на {endpoint}')
    with open(Path(__file__).parent.parent.joinpath(f'schemas/request/{endpoint}.json')) as file:
        validate(data, schema=json.loads(file.read()))

    response = request_with_logs(f"https://yasno.live/api/v1/public/therapists/{endpoint}", method,
                                 data)
    assert response.status_code == 200

    with open(Path(__file__).parent.parent.joinpath(f'schemas/response/{endpoint}.json')) as file:
        validate(response.json(), schema=json.loads(file.read()))

    return response
