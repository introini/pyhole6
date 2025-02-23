from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import Pyhole6


class BaseResource:
    def __init__(self, client: 'Pyhole6'):
        self._client = client

    async def _make_request(self, method, endpoint, **kwargs):
        if not self._client.session_obj.valid:
            raise RuntimeError("Client is not authenticated. Call connect() first.")

        kwargs.setdefault('headers', {})
        kwargs['headers']['sid'] = self._client.session_obj.sid

        async with self._client.session.request(
                method,
                f"{self._client.base_url}/{endpoint}",
                **kwargs
        ) as response:
            return await response.json()