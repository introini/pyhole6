import aiohttp
import logging
from datetime import datetime

class LocalTimeFormatter(logging.Formatter):
    def formatTime(self, record, date_format=None):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Pyhole6(object):

    def __init__(self, base_url, password):
        self.base_url = f"{base_url}/api"
        self.password = password
        self.session = None
        self.session_obj = None
        self.logger = self.configure_logging()

    @staticmethod
    def configure_logging():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = LocalTimeFormatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        await self.authenticate()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.logout()
        await self.session.close()

    async def connect(self):
        self.session = aiohttp.ClientSession()
        await self.authenticate()

    async def disconnect(self):
        await self.logout()
        if self.session:
            await self.session.close()

    async def get_sessions(self):
        if self.session:
            async with self.session.get(f"{self.base_url}/auth/sessions", headers={"sid": self.session_obj.get("sid")}) as response:
                status = response.status
                if status == 200:
                    return await response.json()

    async def authenticate(self):
        self.logger.info(f"Authenticating with {self.base_url}")
        async with self.session.post(f"{self.base_url}/auth", json={"password": self.password}) as response:
            data = await response.json()
            if data.get("session").get("valid"):
                self.session_obj = data.get("session")
            else:
                msg = f"Authentication failed. {data.get("session").get("message")}"
                self.logger.error(msg)
                raise Exception(f"Authentication failed.\n{data.get("session").get("message")}")


    async def logout(self):
        if self.session_obj.get("sid"):
            await self.session.delete(f"{self.base_url}/auth", headers={"sid": self.session_obj.get("sid")})

    async def get_stats(self):
        async with self.session.get(f"{self.base_url}/stats/summary", headers={"sid": self.session_obj.get("sid")}) as response:
            return await response.json()

    async def disable_blocking(self, duration=None):
        async with self.session.post(f"{self.base_url}/dns/blocking",
                                     json={"blocking": False, "timer": duration},
                                     headers={"sid": self.session_obj.get("sid")}) as response:
            data = await response.json()
            if response.status == 200:
                if duration:
                    self.logger.info(f"Disabling ad blocking for {duration}.")
                else:
                    self.logger.info(f"Disabling ad blocking indefinitely.")
                return data
            else:
                msg = f"Unable to disable blocking. {data.get("session").get("message")}"
                self.logger.error(msg)
                raise Exception(f"Error disabling blocking.\n{data.get("session").get("message")}")

    async def enable_blocking(self, duration=None):
        async with self.session.post(f"{self.base_url}/dns/blocking",
                                     json={"blocking": True, "timer": duration},
                                     headers={"sid": self.session_obj.get("sid")}) as response:
            data = await response.json()
            if response.status == 200:
                if duration:
                    self.logger.info(f"Enabling ad blocking for {duration}.")
                else:
                    self.logger.info(f"Enabling ad blocking indefinitely.")
                return data
            else:
                msg = f"Unable to disable blocking. {data.get("session").get("message")}"
                self.logger.error(msg)
                raise Exception(f"Error disabling blocking.\n{data.get("session").get("message")}")

    async def get_blocking_status(self):
        async with self.session.get(f"{self.base_url}/dns/blocking",
                                     headers={"sid": self.session_obj.get("sid")}) as response:
            return await response.json()

    async def get_host_info(self):
        async with self.session.get(f"{self.base_url}/info/host",
                                     headers={"sid": self.session_obj.get("sid")}) as response:
            return await response.json()

    async def get_version_info(self):
        async with self.session.get(f"{self.base_url}/info/version",
                                     headers={"sid": self.session_obj.get("sid")}) as response:
            return await response.json()
