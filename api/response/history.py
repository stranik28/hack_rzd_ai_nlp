from api.response.base import BaseModel
from pydantic import Field

from db.models.history import DBHistory


class HistoryResponse(BaseModel):
    title: str = Field(...)
    department: str = Field(...)
    status: str = Field(...)
    time: str = Field(...)

class HistoryResponseFactory:

    @staticmethod
    def get_from_model(model: DBHistory) -> HistoryResponse:
        return HistoryResponse(
            title=model.title,
            time=model.time,
            status=model.status,
            department=model.department
        )

    @classmethod
    def get_from_models(cls, models: list[DBHistory]) -> list[HistoryResponse]:
        return [cls.get_from_model(model) for model in models]