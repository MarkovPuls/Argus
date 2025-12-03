import httpx
import allure
from clients.api_client import BaseClient
from common.decorators import log_request, measure_time
from models.models import ResponseModel


class HttpxClient(BaseClient):
    @allure.step('GET Httpx')
    @log_request('GET Httpx')
    @measure_time
    def get(self, url: str, **kwargs):
        with httpx.Client() as client:
            res = client.get(url, **kwargs)
        return ResponseModel(code=res.status_code, status=res.reason_phrase, response=res.json() if res.text else None,
                             time=None)

    @allure.step('POST Httpx')
    @log_request('POST Httpx')
    @measure_time
    def post(self, url: str, json=None, **kwargs):
        with httpx.Client() as client:
            res = client.post(url, json=json, **kwargs)
        return ResponseModel(code=res.status_code, status=res.reason_phrase, response=res.json() if res.text else None,
                             time=None)

    @allure.step('PUT Httpx')
    @log_request('PUT Httpx')
    @measure_time
    def put(self, url: str, json=None, **kwargs):
        with httpx.Client() as client:
            res = client.put(url, json=json, **kwargs)
        return ResponseModel(code=res.status_code, status=res.reason_phrase, response=res.json() if res.text else None,
                             time=None)

    @allure.step('DELETE Httpx')
    @log_request('DELETE Httpx')
    @measure_time
    def delete(self, url: str, **kwargs):
        with httpx.Client() as client:
            res = client.delete(url, **kwargs)
        return ResponseModel(code=res.status_code, status=res.reason_phrase, response=res.json() if res.text else None,
                             time=None)
