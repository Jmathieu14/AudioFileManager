# Author: Jacques Mathieu
# Created on 1/24/2020 at 10:03 PM
# Part of the AudioFileManager project

import src.view_ui_to_py.ui_settings as ui_settings
import gui
import sys
import config
from PyQt5.QtWidgets import QFrame
from PyQt5 import QtWidgets


class SettingsView(QFrame):

    def __init__(self):
        super(SettingsView, self).__init__()
        self.ui = ui_settings.Ui_Frame()
        self.ui.setupUi(self)
        self.inject_values()
        self.configure_buttons()

    def inject_values(self):
        self.ui.editsPathEdit.setText(config.get_editing_folder())
        self.ui.dlDirectPathEdit.setText(config.get_downloads_folder())
        self.ui.destPathEdit.setText(config.get_destination_folder())

    def save_settings(self):
        edits_path = self.ui.editsPathEdit.text().strip()
        downloads_path = self.ui.dlDirectPathEdit.text().strip()
        destination_path = self.ui.destPathEdit.text().strip()

        if (edits_path != ""):
            config.update_editing_folder(edits_path)
        if (downloads_path != ""):
            config.update_downloads_folder(downloads_path)
        if (destination_path != ""):
            config.update_destination_folder(destination_path)

    def __open_edits_folder_browser(self):
        gui.open_folder_browser_from_widget(self.ui.editsPathEdit)

    def __open_downloads_folder_browser(self):
        gui.open_folder_browser_from_widget(self.ui.dlDirectPathEdit)

    def __open_destination_folder_browser(self):
        gui.open_folder_browser_from_widget(self.ui.destPathEdit)

    def configure_open_file_dialogs(self):
        self.ui.editsSearchBtn.clicked.connect(self.__open_edits_folder_browser)
        self.ui.dlSearchBtn.clicked.connect(self.__open_downloads_folder_browser)
        self.ui.destSearchBtn.clicked.connect(self.__open_destination_folder_browser)

    def configure_save_button(self):
        self.ui.settingsSaveBtn.clicked.connect(self.save_settings)

    def configure_buttons(self):
        self.configure_save_button()
        self.configure_open_file_dialogs()



if __name__ == "__main__":
    # TODO: remove the config main function call for actual app to work :)
    config.main()
    app = QtWidgets.QApplication(sys.argv)
    settings_view = SettingsView()
    settings_view.show()
    sys.exit(app.exec_())
