import datetime
from typing import List, Optional, Tuple

from .. import Pyhole6Error
from ..models import HistoryEntry, HistoryDBEntry
from .base import BaseResource


class HistoryResource(BaseResource):
    async def list(self) -> List[HistoryEntry]:
        """
        Fetch query history from Pi-hole

        Returns:
            List of HistoryEntry objects
        """

        data = await self._make_request('GET', 'history')

        return [HistoryEntry.from_dict(entry) for entry in data['history']]

    async def clients(self, count: Optional[int] = None) -> HistoryDBEntry:
        """
        Fetch Long term stats data related from Pi-hole

        Returns:
            Long term data
        """
        params = {'N': count} if count else {}

        data = await self._make_request('GET', f'history/clients', params=params)
        return data


    async def database(self, date_range: Tuple, endpoint: Optional[str] = None) -> HistoryDBEntry:
        """
        Fetch Long term stats data related from Pi-hole

        Returns:
            Long term data
        """
        params = {'from': date_range[0], 'until': date_range[1]}

        data = await self._make_request('GET', f'history/database/{endpoint}', params=params)
        return data
