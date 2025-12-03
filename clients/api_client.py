import allure
from abc import ABC, abstractmethod
from settings import base_settings
from clients.routers import APIRoutes


class BaseClient(ABC):
    @abstractmethod
    def get(self, url: str, **kwargs):
        pass

    @abstractmethod
    def post(self, url: str, json=None, **kwargs):
        pass

    @abstractmethod
    def put(self, url: str, json=None, **kwargs):
        pass

    @abstractmethod
    def delete(self, url: str, **kwargs):
        pass


class APIClient:
    def __init__(self, http_client: BaseClient):
        self._client = http_client
        self._base_url = f"{base_settings.api_url.rstrip('/')}/api"

    def _url(self, route: APIRoutes, resource_id=None):
        url = f"{self._base_url}/{route.value}"
        return f"{url}/{resource_id}" if resource_id else url

    @allure.step("GET")
    def get(self, route: APIRoutes, resource_id=None, **kwargs):
        return self._client.get(self._url(route, resource_id), **kwargs)

    @allure.step("POST")
    def post(self, route: APIRoutes, resource_id=None, json=None, **kwargs):
        return self._client.post(self._url(route, resource_id), json=json, **kwargs)

    @allure.step("PUT")
    def put(self, route: APIRoutes, resource_id, json=None, **kwargs):
        return self._client.put(self._url(route, resource_id), json=json, **kwargs)

    @allure.step("DELETE")
    def delete(self, route: APIRoutes, resource_id, **kwargs):
        return self._client.delete(self._url(route, resource_id), **kwargs)
