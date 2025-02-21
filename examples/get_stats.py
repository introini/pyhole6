from pyhole6 import Pyhole6
import asyncio

async def main():
    client = Pyhole6("http://pi.hole", "password_or_api_ley")
    await client.connect()

    stats = await client.get_stats()

    for k,v in stats.items():
        print(k,v)

    await client.disconnect()

asyncio.run(main())