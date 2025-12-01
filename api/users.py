from api.routers import APIRoutes


class UsersAPI:
    """API обертка для сущности Users"""

    def __init__(self, client, base_url: str):
        self.client = client
        self.base_url = base_url

    def get_user(self, user_id: int):
        return self.client.get(f'{self.base_url}/{APIRoutes.PLAN}/{user_id}')
