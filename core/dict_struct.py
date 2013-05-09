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
class DictStruct:
    def __init__(self, **entries):
        """
        Transforms a simple dict object into a structured object

        @type entries: dict
        @param entries: The dict to be transformed into struct
        """
        for key, value in entries.items():
            if type(value) == dict:
                entries[key] = DictStruct(**value)
        self.__dict__.update(entries)

    def __str__(self):
        formated = "[Struct instance ; Object id {id}]\n".format(id=id(self))
        formated += "=" * 80
        formated += self._prettyString()
        formated += "=" * 80
        return formated

    def _prettyString(self, ident=0):
        buffer = ""
        for i in dir(self):
            if re.match(r"__[a-z]+__", i) is None and i != "_prettyString":
                if self.__dict__[i].__class__.__name__ == 'Struct':
                    buffer += "\n" + ("\t" * ident) + i + ":\n"
                    buffer += self.__dict__[i]._prettyString(ident+1)

                else:
                    buffer += ("\t" * ident) + i +": "
                    buffer += str(self.__dict__[i]) + " {valType}\n".format(valType=type(self.__dict__[i]))

        return buffer