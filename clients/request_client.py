import requests
import logging
import allure
from clients.base import BaseClient
from common.fixtures import log_request, measure_time
from models.models import ResponseModel

logger = logging.getLogger('RequestsClient')


class RequestsClient(BaseClient):
    @allure.step('GET Requests')
    @log_request('GET Requests')
    @measure_time
    def get(self, url, **kwargs):
        res = requests.get(url, **kwargs)
        return ResponseModel(code=res.status_code, status=res.reason, response=res.json(), time=None)

    @allure.step('POST Requests')
    @log_request('POST Requests')
    def post(self, url, json=None, **kwargs):
        res = requests.post(url, json=json, **kwargs)
        return ResponseModel(code=res.status_code, status=res.reason, response=res.json(), time=None)

    @allure.step('PUT Requests')
    @log_request('PUT Requests')
    def put(self, url, json=None, **kwargs):
        res = requests.post(url, json=json, **kwargs)
        return ResponseModel(code=res.status_code, status=res.reason, response=res.json(), time=None)

    @allure.step('DELETE Requests')
    @log_request('DELETE Requests')
    def delete(self, url, **kwargs):
        res = requests.delete(url, **kwargs)
        return ResponseModel(code=res.status_code, status=res.reason, response=res.json(), time=None)
