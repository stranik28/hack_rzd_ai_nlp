from db.repository.base import BaseModel
from sqlalchemy import (
    Column,
    String
)


class DBHistory(BaseModel):
    __tablename__ = 'history'
    title = Column(String, nullable=True)
    department = Column(String, nullable=True)
    status = Column(String, nullable=True)
    time = Column(String, nullable=True)
