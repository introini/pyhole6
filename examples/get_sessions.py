from pyhole6 import Pyhole6
import asyncio

async def main():
    client = Pyhole6("http://pi.hole", "password_or_api_ley")
    await client.connect()

    # Loop through a list of sessions
    sessions  = await client.get_sessions()
    for s in sessions.get("sessions"):
        print(s)

    await client.disconnect()

asyncio.run(main())