from enum import Enum


class APIRoutes(Enum):
    PEOP = 'people'
    PLAN = 'planets'
    FILM = 'films'
    SPEC = 'species'
    VEHI = 'vehicles'
    STAR = 'starships'

    def __str__(self) -> str:
        return self.value


class ErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Response code is not correct'
    WRONG_STATUS = 'Response status is not correct'
    WRONG_TIME = f'Long execution time'
    WRONG_FIELDS_RESPONSE = 'Incorrect fields in the response'
    WRONG_RESPONSE = 'Incorrect response'
