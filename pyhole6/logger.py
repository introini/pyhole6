import logging
from datetime import datetime


class LocalTimeFormatter(logging.Formatter):
    def formatTime(self, record, date_format=None):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = LocalTimeFormatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger