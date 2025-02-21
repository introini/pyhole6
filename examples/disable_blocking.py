from pyhole6 import Pyhole6
import asyncio

async def main():
    client = Pyhole6("http://pi.hole", "password_or_api_ley")
    await client.connect()

    # Disable blocking indefinitely
    await client.disable_blocking()

    # Disable blocking for 5 minutes
    await client.disable_blocking(duration=300)

    await client.disconnect()

asyncio.run(main())