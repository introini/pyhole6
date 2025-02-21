from pyhole6 import Pyhole6
import asyncio

async def main():
    client = Pyhole6("http://pi.hole", "password_or_api_ley")
    await client.connect()

    host_info  = await client.get_host_info()

    await client.disconnect()

asyncio.run(main())