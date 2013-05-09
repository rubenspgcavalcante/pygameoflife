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

import re

class TypeParser(object):
    def __init__(self):
        pass

    def tuple(self, value, type):
        """
        Parse a string value into a tuple of the given type

        @type value: str
        @param value: The string value to convert
        @type type: str
        @param type: The type of tuple to convert, e.g: int
        @rtype : tuple
        """
        resList = re.sub(r'\(*\)*\ *', r"", value).split(",")
        for key, value in enumerate(resList):
            if type == "int":
                resList[key] = int(value)

            elif type == "float":
                resList[key] = float(value)

            elif type == "str":
                resList[key] = str(value)

        return tuple(resList)

    def int(self, value):
        """
        Convert a string into a integer

        @type value: str
        @param value: The string to convert e.g: "10"
        @rtype: int
        """
        return int(value.replace(" ", ""))

    def float(self, value):
        """
        Convert a string into a float
        @type value: str
        @param value: The string to convert e.g: "10"
        @rtype: float
        """
        return float(value.replace(" ", ""))