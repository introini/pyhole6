from typing import List, Optional
from ..models import HistoryEntry
from .base import BaseResource


class HistoryResource(BaseResource):
    async def list(self, limit: Optional[int] = None) -> List[HistoryEntry]:
        """
        Fetch query history from Pi-hole

        Args:
            limit: Optional number of entries to return

        Returns:
            List of HistoryEntry objects
        """
        params = {'limit': limit} if limit else {}
        data = await self._make_request('GET', 'history', params=params)
        return [HistoryEntry.from_dict(entry) for entry in data['history']]
