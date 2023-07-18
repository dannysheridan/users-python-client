# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BadRequestErrorResponseBodyCode(str, enum.Enum):
    INVALID_REQUEST_ERROR = "invalid_request_error"
    INTENT_REQUEST_ERROR = "intent_request_error"

    def visit(
        self, invalid_request_error: typing.Callable[[], T_Result], intent_request_error: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is BadRequestErrorResponseBodyCode.INVALID_REQUEST_ERROR:
            return invalid_request_error()
        if self is BadRequestErrorResponseBodyCode.INTENT_REQUEST_ERROR:
            return intent_request_error()
