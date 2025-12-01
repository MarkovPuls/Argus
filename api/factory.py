from api.users import UsersAPI


class APIFactory:
    """
    Фабрика API классов.
    Принимает HTTP клиент, а дальше возвращает нужные API-обертки.
    """

    def __init__(self, client, base_url: str):
        self.client = client
        self.base_url = base_url

    @property
    def users(self) -> UsersAPI:
        return UsersAPI(client=self.client, base_url=self.base_url)
