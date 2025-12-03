import allure
import pytest
from clients.routers import APIRoutes, ErrorMessages
from models.schemas import Planet


@pytest.mark.api
@allure.story('users_get')
class TestPlanetsGet:
    @allure.title('1. Проверка кода и статуса ответа')
    @pytest.mark.parametrize('plan_id', [1, 2, 3, 4, 5])
    def test_status_code(self, api_client, plan_id):
        response = api_client.get(APIRoutes.PLAN, plan_id)
        assert response.code == 200, ErrorMessages.WRONG_STATUS_CODE.value
        assert response.status == 'OK', ErrorMessages.WRONG_STATUS.value

    @allure.title('2. Время выполнения метода, меньше 500 ms')
    def test_time(self, api_client):
        response = api_client.get(APIRoutes.PLAN, 1)
        assert response.time < 500, ErrorMessages.WRONG_TIME.value

    @allure.title('3. Проверка полей ответа')
    def test_validate_json(self, api_client):
        response = api_client.get(APIRoutes.PLAN, 1)
        assert Planet.model_validate(response.response), ErrorMessages.WRONG_FIELDS_RESPONSE.value
