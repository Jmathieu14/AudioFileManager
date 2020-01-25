# Author: Jacques Mathieu
# Created on 1/24/2020 at 10:03 PM
# Part of the AudioFileManager project

import src.view_ui_to_py.ui_settings as ui_settings
import sys
from PyQt5.QtWidgets import QFrame
from PyQt5 import QtWidgets

class SettingsView(QFrame):
    def __init__(self):
        super(SettingsView, self).__init__()
        self.ui = ui_settings.Ui_Frame()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    settings_view = SettingsView()
    settings_view.show()
    sys.exit(app.exec_())
