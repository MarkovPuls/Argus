from enum import Enum


class APIRoutes(str, Enum):
    METR = '/metrics'

    def __str__(self) -> str:
        return self.value


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Response code is not correct'
    WRONG_TIME = f'Long execution time'
    WRONG_FIELDS_RESPONSE = 'Incorrect fields in the response'
    WRONG_RESPONSE = 'Incorrect response'
