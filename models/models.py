from pydantic import BaseModel, Field
from settings import base_set


class ResponseModel:
    def __init__(self, code: int, status: str = None, response: dict = None, cook: str = None, time: float = None,
                 headers: str = None):
        self.code = code
        self.status = status
        self.response = response
        self.cook = cook
        self.time = time
        self.headers = headers


class LoginSuperModel(BaseModel):
    username: str = Field(default=base_set.test_user.login)
    password: str = Field(default=base_set.test_user.password)
