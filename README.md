# pyhole6 API Client

![Version](https://img.shields.io/badge/version-0.0.2-blue.svg)

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
from pyhole6 import pyhole6
import asyncio

async def main():
    client = pyhole6("http://pi.hole", "your_password")
    await client.connect()
    # Use the client here
    await client.disconnect()

asyncio.run(main())
```

### Using as a Context Manager

```
async with pyhole6("http://pi.hole", "your_password") as client:
    # Use the client here
```

### Available Methods

#### Get Statistics

```
stats = await client.get_stats()
print(stats)
```

#### Disable Blocking

```
# Disable blocking for 5 minutes (300 seconds)
result = await client.disable_blocking(duration=300)
print(result)
```

#### Enable Blocking

```
# Enable blocking immediately
result = await client.enable_blocking()
print(result)
```

#### Get Blocking Status

```
status = await client.get_blocking_status()
print(status)
```

#### Get Host Information

```
host_info = await client.get_host_info()
print(host_info)
```

#### Get Version Information

```
version_info = await client.get_version_info()
print(version_info)
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
```

---
Answer from Perplexity: pplx.ai/share