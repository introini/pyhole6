from pyhole6 import Pyhole6
import asyncio

async def main():
    client = Pyhole6("http://pi.hole", "password_or_api_ley")
    await client.connect()

    status = await client.get_blocking_status()
    if status.get("blocking") == "enabled":
        await client.disable_blocking()

    print(await client.get_blocking_status())

    await client.disconnect()

asyncio.run(main())