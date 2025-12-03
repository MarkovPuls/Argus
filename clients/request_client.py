import requests
import allure
from clients.api_client import BaseClient
from common.decorators import log_request, measure_time
from models.models import ResponseModel


class RequestsClient(BaseClient):
    @allure.step('GET Requests')
    @log_request('GET Requests')
    @measure_time
    def get(self, url: str, **kwargs):
        res = requests.get(url, **kwargs)
        return ResponseModel(code=res.status_code, status=res.reason, headers=res.headers, response=res.json(),
                             time=None)

    @allure.step('POST Requests')
    @log_request('POST Requests')
    def post(self, url: str, json=None, **kwargs):
        res = requests.post(url, json=json, **kwargs)
        return ResponseModel(code=res.status_code, status=res.reason, headers=res.headers, response=res.json(),
                             time=None)

    @allure.step('PUT Requests')
    @log_request('PUT Requests')
    def put(self, url: str, json=None, **kwargs):
        res = requests.post(url, json=json, **kwargs)
        return ResponseModel(code=res.status_code, status=res.reason, headers=res.headers, response=res.json(),
                             time=None)

    @allure.step('DELETE Requests')
    @log_request('DELETE Requests')
    def delete(self, url: str, **kwargs):
        res = requests.delete(url, **kwargs)
        return ResponseModel(code=res.status_code, status=res.reason, headers=res.headers, response=res.json(),
                             time=None)
