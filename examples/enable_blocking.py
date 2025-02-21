from pyhole6 import Pyhole6
import asyncio

async def main():
    client = Pyhole6("http://pi.hole", "password_or_api_ley")
    await client.connect()

    # Enable blocking indefinitely
    await client.enable_blocking()

    # Enable blocking for 5 minutes
    await client.enable_blocking(duration=300)

    await client.disconnect()

asyncio.run(main())