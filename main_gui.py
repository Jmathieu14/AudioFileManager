# Author: Jacques Mathieu
# Created on 6/27/2019 at 1:48 PM
# The main view handler for the AudioFileManager project

from PyQt5 import uic

import gui as g

# Configuration for populating fields and widgets seen on the main page
POP_CONFIG = {}

# Load the appropriate view
UIClass, QtBaseClass = uic.loadUiType("ui/a_main.ui")


# Class for main view of this application
class MainView(UIClass, QtBaseClass):
    def __init__(self):
        UIClass.__init__(self)
        QtBaseClass.__init__(self)
        self.setupUi(self)


# Open the settings page on settings button click
def open_settings():
    return None


# Initialize the POP CONFIG for this view
def init():
    global POP_CONFIG
    POP_CONFIG = {
        'settings_button': {'obj_name': 'openSettingsBtn',
                            'icon': 'icons/settings [#1491].png',
                            'setText': '',
                            'flat': True,
                            'click': g.show_settings}
    }


# Run the main view
def run_gui():
    init()
    window = MainView()
    window.show()
    g.populate_fields(POP_CONFIG)
    return window
