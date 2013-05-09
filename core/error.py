#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = "Rubens Pinheiro Gonçalves Cavalcante"
__date__ = "08/05/13 19:18"
__licence__ = "GPLv3"
__email__ = "rubenspgcavalcante@gmail.com"

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