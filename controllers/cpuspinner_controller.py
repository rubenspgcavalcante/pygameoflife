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

from core.event import *
from core.controller import *

class CPUSpinnerController(Controller):
	"""..."""
	def __init__(self):
		Controller.__init__(self)
		self.keepGoing = 1

		self.bind(QuitEvent(), self.stop)

	def defaultAction(self):
		pass

	def run(self):
		self.trigger(AppStartEvent())
		while self.keepGoing:
			self.trigger(TickEvent())

	def stop(self, event):
			#this will stop the while loop from running
			self.keepGoing = False