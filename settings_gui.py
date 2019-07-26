# Author: Jacques Mathieu
# Created on 6/16/2019 at 3:33 AM
# Main GUI for the AudioFileManager project


from PyQt5 import QtCore, uic, QtWidgets
import config
import gui as g
import utility as util

# GUI Requirements:
# Settings Button + Page
# |-> Show configured folder paths
# |-> Click folder icon to choose new path, double click text to edit path manually

UIClass, QtBaseClass = uic.loadUiType("ui/settings.ui")

# Configuration for populating fields and widgets seen on the settings page
POP_CONFIG = {}


class SettingsView(UIClass, QtBaseClass):
    def __init__(self):
        UIClass.__init__(self)
        QtBaseClass.__init__(self)
        self.setupUi(self)


# Take text from each line and save to config file
def settings_save():
    widgets = g.get_widgets()
    print("Saving settings...")
    line_edit_fields = [
        {"name": "dlDirectPathEdit", "f": "update_downloads_folder"},
        {"name": "editsPathEdit", "f": "update_editing_folder"},
        {"name": "destPathEdit", "f": "update_destination_folder"}
    ]
    for w in widgets:
        for line in line_edit_fields:
            if w.objectName() == line['name']:
                line_text = getattr(QtWidgets.QLineEdit, "text")(w)
                # Only update if text is not empty
                if line_text != "":
                    getattr(config, line['f'])(path=line_text)


# Open folder browser for download path section
def open_dl_folder_browser():
    g.open_folder_browser('dlDirectPathEdit')


# Open folder browser for download path section
def open_edit_folder_browser():
    g.open_folder_browser('editsPathEdit')


# Open folder browser for download path section
def open_dest_folder_browser():
    g.open_folder_browser('destPathEdit')


# Initialize the POP CONFIG for this view
def init():
    global POP_CONFIG
    POP_CONFIG = {
        # This layout assumes the gui args will be the QWidget selected
        'save_button': {'obj_name': 'settingsSaveBtn',
                        'click': settings_save
                        },
        'dl_button': {'obj_name': 'dlSearchBtn',
                      'click': open_dl_folder_browser,
                      'icon': 'icons/folder [#1793].png',
                      'setText': '',
                      'flat': True
                      },
        'edit_button': {'obj_name': 'editsSearchBtn',
                        'click': open_edit_folder_browser,
                        'icon': 'icons/folder [#1793].png',
                        'setText': '',
                        'flat': True
                        },
        'dest_button': {'obj_name': 'destSearchBtn',
                        'click': open_dest_folder_browser,
                        'icon': 'icons/folder [#1793].png',
                        'setText': '',
                        'flat': True
                        },
        'cancel_button': {'obj_name': 'settingsCancelBtn',
                          'click': g.show_main},
        'dl_path': {'obj_name': 'dlDirectPathEdit',
                    'fmod': config,
                    'fname': 'get_downloads_folder',
                    'fargs': {},
                    'gmod': QtWidgets.QLineEdit,
                    'g_fname': 'setText'
                    },
        'edit_path': {'obj_name': 'editsPathEdit',
                      'fmod': config,
                      'fname': 'get_editing_folder',
                      'fargs': {},
                      'gmod': QtWidgets.QLineEdit,
                      'g_fname': 'setText'
                      },
        'final_path': {'obj_name': 'destPathEdit',
                       'fmod': config,
                       'fname': 'get_destination_folder',
                       'fargs': {},
                       'gmod': QtWidgets.QLineEdit,
                       'g_fname': 'setText'
                       }
    }


# Run the gui for the settings page
def run_gui():
    init()
    window = SettingsView()
    window.show()
    g.populate_fields(POP_CONFIG)
    return window
