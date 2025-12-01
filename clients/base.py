class BaseClient:
    """Базовый клиент. Определяет интерфейс для всех клиентов."""

    def get(self, url, **kwargs):
        raise NotImplementedError

    def post(self, url, json=None, **kwargs):
        raise NotImplementedError
