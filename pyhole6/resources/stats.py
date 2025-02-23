import datetime
from typing import List, Optional, Tuple

from .. import Pyhole6Error
from ..models import StatsEntry
from .base import BaseResource


class StatsResource(BaseResource):
    async def summary(self) -> StatsEntry:
        """
        Fetch stats summary from Pi-hole

        Returns:
            List of StatsSummary objects
        """
        data = await self._make_request('GET', 'stats/summary')
        return data

    async def top_clients(self, blocked: Optional[bool] = False, count: Optional[int] = 10) -> StatsEntry:
        """
        Fetch Top Clients from Pi-hole

        Returns:
            List of HistoryEntry objects
        """
        params = {'blocked': f"{blocked}", 'count': count}

        data = await self._make_request('GET', 'stats/top_clients', params=params)
        return data

    async def top_domains(self, blocked: Optional[bool] = False, count: Optional[int] = 10) -> StatsEntry:
        """
        Fetch Top Clients from Pi-hole

        Returns:
            List of HistoryEntry objects
        """
        params = {'blocked': f"{blocked}", 'count': count}

        data = await self._make_request('GET', 'stats/top_domains', params=params)
        return data

    async def upstreams(self) -> StatsEntry:
        """
        Fetch Top Clients from Pi-hole

        Returns:
            List of HistoryEntry objects
        """

        data = await self._make_request('GET', 'stats/upstreams')
        return data

    async def recent_blocked(self, count: Optional[int] = 1) -> StatsEntry:
        """
        Fetch Top Clients from Pi-hole

        Returns:
            List of HistoryEntry objects
        """

        data = await self._make_request('GET', 'stats/recent_blocked')
        return data

    async def query_types(self) -> StatsEntry:
        """
        Fetch Top Clients from Pi-hole

        Returns:
            List of HistoryEntry objects
        """

        data = await self._make_request('GET', 'stats/query_types')
        return data

    async def database(self, endpoint: str, date_range: Tuple, **kwargs) -> StatsEntry:
        """
        Fetch Top Clients from Pi-hole

        Returns:
            List of HistoryEntry objects
        """
        params = {'from': date_range[0], 'until': date_range[1]}
        params.update(kwargs)

        if 'blocked' in params:
            params['blocked'] = f"{params.get('blocked')}"
        data = await self._make_request('GET', f'stats/database/{endpoint}', params=params)
        return data
