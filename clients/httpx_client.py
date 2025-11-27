import allure
from httpx import Client, Response


class ClientHTTPx:
    def __init__(self, sync_client=None):
        self.sync_client: Client = sync_client

    @allure.step('Making sync client request')
    def sync_custom_request(self, method: str, url: str, **kwargs) -> Response:
        request = self.sync_client.build_request(method, url, **kwargs)
        return self.sync_client.send(request)
