from pyhole6 import Pyhole6
import asyncio

async def main():
    client = Pyhole6("http://pi.hole", "password_or_api_ley")
    await client.connect()

    version_info = await client.get_version_info()

    for k,v in version_info.items():
        print(k,v)

    await client.disconnect()

asyncio.run(main())