from settings import base_set
from routers import APIRoutes
from models.models import ResponseModel
import logging

logger = logging.getLogger("Custom log metrics")


class Swapi:
    def __init__(self, client):
        self.url = base_set.api_url
        self.client = client

    async def metrics_get(self, page: int = None):
        response = self.client.custom_request("GET", f"{self.url}{APIRoutes.METR}", params=page)
        logger.info(f'В GET metrics получаем код ответа: {response.status_code}')
        return ResponseModel(status=response.status_code, response=response.json(), headers=response.headers)
