import json
import os

import allure
from helpers.attaches import request_with_logs
from jsonschema import validate
from pathlib import Path


def send_request(endpoint, method, data=''):
    allure.step(f'Делаем запрос на {endpoint}')
    if not (data == '' or method == 'get'):
        with open(Path(__file__).parent.parent.joinpath(f'schemas/request/{endpoint}.json')) as file:
            validate(data, schema=json.loads(file.read()))

    response = request_with_logs(f"{os.getenv("BASE_URL")}/api/v1/public/therapists/{endpoint}", method,
                                 data)

    with open(Path(__file__).parent.parent.joinpath(f'schemas/response/{endpoint}.json')) as file:
        validate(response.json(), schema=json.loads(file.read()))

    return response


def check_response_code(response, code):
    allure.step(f'Проверям статус ответа от сервера')
    assert response.status_code == code
