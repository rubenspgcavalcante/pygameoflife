import logging
from core.logger import Logger


class GenericError(Exception):
    def __init__(self, message, originalException=None):
        """
        A generic system exception
        @type message: str
        @param message: The exception message
        @type originalException: Exception
        @param originalException: The original exception raised
        """

        logger = Logger(level=logging.ERROR)
        if originalException is not None:
            message += "\nOriginal exception:\n\t" + originalException.message

        Exception.__init__(self, message)
        logger.log(message)

class CacheError(GenericError):
    def __init__(self, originalException=None):
        GenericError.__init__(self, "Cache file error", originalException=originalException)