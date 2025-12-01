from pydantic import ValidationError, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class TestUser(BaseSettings):
    login: str = Field(default='')
    password: str = Field(default='')


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    base_url: str
    test_user: TestUser = TestUser()

    @property
    def api_url(self) -> str:
        return f'https://{self.base_url}/api/'


try:
    base_set = Settings()
except ValidationError as e:
    print('Validation Error in settings:', e)
    raise
