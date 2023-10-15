from sqlalchemy import select

from db.models.history import DBHistory
from db.repository.base import BaseRepository


class HistoryRepository(BaseRepository):

    async def history_all(self):
        query = (
            select(DBHistory)
            .select_from(DBHistory)
        )

        return await self.all_ones(query)
