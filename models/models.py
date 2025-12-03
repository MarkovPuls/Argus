from pydantic import BaseModel, Field
from settings import base_settings


class ResponseModel:
    def __init__(
            self,
            code: int,
            status: str = None,
            response: dict | str | None = None,
            cook: str = None,
            time: float = None,
            headers: dict | None = None,
    ):
        self.code = code
        self.status = status
        self.response = response
        self.cook = cook
        self.time = time
        self.headers = headers

    def json(self):
        return self.response


class LoginSuperModel(BaseModel):
    username: str = Field(default=base_settings.test_user.login)
    password: str = Field(default=base_settings.test_user.password)
