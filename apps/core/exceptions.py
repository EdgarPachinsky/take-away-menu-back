from typing import Union

from rest_framework.exceptions import ValidationError, NotFound, AuthenticationFailed


class BaseValidationError(ValidationError):

    def __init__(self, detail: Union[str, list, dict] = None, error_code=None, code=None):
        if isinstance(detail, str):
            detail = {'detail': detail}
        if error_code:
            detail['error_code'] = error_code
        super().__init__(detail, code)


class BaseAuthenticationFailedError(AuthenticationFailed):

    def __init__(self, detail: Union[str, list, dict] = None, code=None):
        if isinstance(detail, str):
            detail = {'detail': detail}

        super().__init__(detail, code)


class BaseNotFoundError(NotFound):

    def __init__(self, detail: Union[str, list, dict] = None, code=None):
        if isinstance(detail, str):
            detail = {'detail': detail}

        super().__init__(detail, code)
