from pyhole6 import Pyhole6
import asyncio

async def main():
    async with Pyhole6("http://pi.hole", "password_or_api_ley") as client:

     stats = await client.get_stats()



asyncio.run(main())