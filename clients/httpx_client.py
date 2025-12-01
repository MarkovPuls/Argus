import httpx
import logging
import allure
from clients.base import BaseClient
from common.fixtures import log_request, measure_time
from models.models import ResponseModel

logger = logging.getLogger('HttpxClient')


class HttpxClient(BaseClient):
    @allure.step('GET Httpx')
    @log_request('GET Httpx')
    @measure_time
    def get(self, url, **kwargs):
        with httpx.Client() as client:
            res = client.get(url, **kwargs)
        return ResponseModel(code=res.status_code, status=res.reason_phrase, response=res.json(), time=None)

    @allure.step('POST Httpx')
    @log_request('POST Httpx')
    @measure_time
    def post(self, url, json=None, **kwargs):
        with httpx.Client() as client:
            res = client.post(url, json=json, **kwargs)
        return ResponseModel(code=res.status_code, status=res.reason_phrase, response=res.json(), time=None)

    @allure.step('PUT Httpx')
    @log_request('PUT Httpx')
    @measure_time
    def put(self, url, json=None, **kwargs):
        with httpx.Client() as client:
            res = client.put(url, json=json, **kwargs)
        return ResponseModel(code=res.status_code, status=res.reason_phrase, response=res.json(), time=None)

    @allure.step('DELETE Httpx')
    @log_request('DELETE Httpx')
    @measure_time
    def delete(self, url, **kwargs):
        with httpx.Client() as client:
            res = client.delete(url, **kwargs)
        return ResponseModel(code=res.status_code, status=res.reason_phrase, response=res.json(), time=None)
