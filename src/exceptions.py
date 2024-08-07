from typing import Union, Optional


class BaseError(Exception):
    MESSAGE = "Неизвестная ошибка"

    def __init__(self, value: Optional[Union[str, int]] = None) -> None:
        super().__init__(self.MESSAGE.format(value))
        self.value = value


class FailedFetchError(BaseError):
    MESSAGE = "Failed attempt to fetch data from {}"


class FailedResponseError(BaseError):
    MESSAGE = "Failed response: {}"
