import pytest
import logging
from clients.request_client import RequestsClient
from clients.httpx_client import HttpxClient
from api.factory import APIFactory
from settings import base_set

url = f'{base_set.base_url}/api'


def pytest_addoption(parser):
    parser.addoption(
        '--client',
        action='store',
        default='requests',
        choices=['requests', 'httpx'],
        help='Выбор HTTP клиента'
    )


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
)


@pytest.fixture(scope='session')
def client(request):
    option = request.config.getoption('--client')
    logging.info(f'### SELECTED CLIENT: {option}')
    return RequestsClient() if option == 'requests' else HttpxClient()


@pytest.fixture(scope='session')
def api(client):
    logging.info('### API FACTORY INITIALIZED')
    return APIFactory(client=client, base_url=url)
