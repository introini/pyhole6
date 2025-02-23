import datetime
from typing import List, Optional, Tuple
from ..models import BlockingStatus
from .base import BaseResource


class DNSResource(BaseResource):
    async def status(self):
        data = await self._make_request('GET', 'dns/blocking')
        return BlockingStatus.from_dict(data)

    async def enable(self, timer: Optional[int] = None):

        params = {'blocking': True, 'timer': timer}
        data = await self._make_request('POST', 'dns/blocking', json=params)
        return BlockingStatus.from_dict(data)

    async def disable(self, timer: Optional[int] = None):

        params = {'blocking': False, 'timer': timer}
        data = await self._make_request('POST', 'dns/blocking', json=params)
        return BlockingStatus.from_dict(data)