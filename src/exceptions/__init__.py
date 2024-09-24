import werkzeug
from typing import Any


class APIHTTPException(werkzeug.exceptions.HTTPException):
    def __init__(self, description: str, error_code: str, causes: Any = None):
        super(APIHTTPException, self).__init__()
        if causes is None:
            causes = []
        self.data = {"errorCode": error_code, "errorMessage": description, "errorCauses": causes}


class UnauthorizedError(APIHTTPException):
    code = 401
    description = "Unauthorized: Access denied"
    error_code = "E10200"

    def __init__(self, causes: Any = None):
        super(UnauthorizedError, self).__init__(description=self.description, error_code=self.error_code, causes=causes)


class InvalidInputError(APIHTTPException):
    code = 400
    description = "Invalid Input Error"
    error_code = "E10100"

    def __init__(self, causes: Any = None):
        super(InvalidInputError, self).__init__(
            description=self.description,
            error_code=self.error_code,
            causes=causes)


class RequestBodyValidationError(APIHTTPException):
    code = 400
    description = "The request body was not well-formed."
    error_code = "E10101"

    def __init__(self, causes: Any = None):
        super(RequestBodyValidationError, self).__init__(
            description=self.description,
            error_code=self.error_code,
            causes=causes,
        )


class UserAlreadyExists(APIHTTPException):
    code = 400
    description = "User Already Exists"
    error_code = "E10102"

    def __init__(self, causes: Any = None):
        super(UserAlreadyExists, self).__init__(
            description=self.description,
            error_code=self.error_code,
            causes=causes,
        )


class UserNotFound(APIHTTPException):
    code = 404
    description = "User Not Found"
    error_code = "E10300"

    def __init__(self, causes: Any = None):
        super(UserNotFound, self).__init__(
            description=self.description,
            error_code=self.error_code,
            causes=causes,
        )


class RepositoryException(Exception):
    def __init__(self, message: str = None):
        super().__init__(message)
        self.message = message
