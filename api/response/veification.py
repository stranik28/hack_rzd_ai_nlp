from typing import Optional

from pydantic import Field

from api.response.base import ResponseBase


class BaseVerify(ResponseBase):
    status: int = Field(...)
    error_message: Optional[str] = Field(None)
    recommendation: Optional[str] = Field(None)
