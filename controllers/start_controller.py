#!/usr/bin/env python
#coding=utf-8

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
__date__ = "08/05/13 22:01"
__licence__ = "GPLv3"
__email__ = "rubenspgcavalcante@gmail.com"

import controllers.pygame_input_controller
from controllers.keyboard_controller import *
from controllers.mouse_controller import *
from controllers.cpuspinner_controller import *
from controllers.display_controller import *
from controllers.launcher_controller import *
from controllers.notification_controller import *
from controllers.sound_effect_controller import *

class StartController(object):
    def __init__(self):
        inputs = controllers.pygame_input_controller.PygameInputController()
        keyboard = KeyboardController()
        mouse = MouseController()
        spinner = CPUSpinnerController()
        launcher = LauncherController()
        notifications = NotificationController()
        sounds = SoundEffectController()

        display = DisplayController()
        spinner.run()