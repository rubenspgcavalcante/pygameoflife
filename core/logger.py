import logging
from core.resource_manager import Resource


class Logger(object):
    def __init__(self, level=logging.INFO):
        self.level = level
        logging.basicConfig(filename=Resource().logFile(), level=level, format="%(asctime)s %(message)s")

    def log(self, message):
        logging.log(level=self.level, msg=message)