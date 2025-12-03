import pytest
from clients.request_client import RequestsClient
from clients.httpx_client import HttpxClient
from clients.api_client import APIClient


def pytest_addoption(parser):
    parser.addoption(
        '--client',
        action='store',
        default='requests',
        choices=['requests', 'httpx'],
        help='Выбор HTTP клиента',
    )


@pytest.fixture(scope='session')
def http_client(request):
    selected = request.config.getoption('--client')
    return RequestsClient() if selected == 'requests' else HttpxClient()


@pytest.fixture(scope='session')
def api_client(http_client):
    return APIClient(http_client)
