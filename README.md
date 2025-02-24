# pyhole6 API Client

![Version](https://img.shields.io/badge/version-0.0.4-blue.svg)

*pyhole6* is an asynchronous Python client for interacting with the Pi-hole v6.0 REST API. It provides a simple interface to perform various operations on your Pi-hole server.

## Features

- Asynchronous API calls using aiohttp
- Automatic session management
- Logging with local timestamps
- Easy-to-use methods for common Pi-hole operations

## Installation

```
pip install pyhole6
```

## Usage

### Initializing the Client

```
from pyhole6 import Pyhole6
import asyncio

async def main():
    client = Pyhole6("http://pi.hole", "your_password")
    await client.connect()
    # Use the client here
    await client.disconnect()

asyncio.run(main())
```

### Using as a Context Manager

```
async with Pyhole6("http://pi.hole", "your_password") as client:
    # Use the client here
```

### Available Methods

#### Statistics

```
stats = await client.stats.summary()
print(stats)


now = datetime.datetime.now()
_from = int(datetime.datetime.timestamp(now - datetime.timedelta(days=3)))
until = int(datetime.datetime.timestamp(now))

top_clients = await client.stats.top_clients(blocked=True, count=5)

# Top 10 clients in the last 3 days
top_clients_date_range = await client.stats.database('top_clients', (_from, until), blocked=False, count=10)

```

#### DNS - Disable Blocking

```
# Disable blocking for 5 minutes (300 seconds)
result = await client.dns.disable(timer=300)

# Disable blocking for indefinitely
result = await client.dns.disable()

```

#### DNS - Enable Blocking

```
# Enable blocking for 5 minutes (300 seconds
result = await client.dns.enable(timer=300)

# Enable blocking indefinitely
result = await client.dns.disable()

```

#### DNS - Get Blocking Status

```
status = await client.dns.status()
print(status)
```



## Logging

The client includes built-in logging with local timestamps. You can access the logger through `client.logger`:

```
client.logger.info("Custom log message")
```

## Error Handling

The client will raise exceptions for authentication failures and other API errors. It's recommended to use try-except blocks when making API calls:

```
try:
    await client.connect()
    stats = await client.get_stats()
except Exception as e:
    print(f"An error occurred: {e}")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GPLv3 License.
