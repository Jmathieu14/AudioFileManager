# Author: Jacques Mathieu
# Created on 1/8/2020 at 9:40 PM
# Part of the AudioFileManager project

from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import sys
import unittest
import src.view_controllers.settings_controller as settings_controller

test_app = QApplication(sys.argv)

class SettingsPageTest(unittest.TestCase):

    def setUp(self):
        self.settings_page = settings_controller.SettingsView()
        self.ui = self.settings_page.ui

    def test_should_have_title(self):
        self.assertEquals(self.ui.settings.text(), "Settings")

    def test_should_have_edits_folder_input_label_and_button(self):
        self.assertIsNotNone(self.ui.editsPathEdit)
        self.assertIsNotNone(self.ui.editsLabel)
        self.assertEquals(self.ui.editsLabel.text(), "Edits:")
        self.assertIsNotNone(self.ui.editsSearchBtn)

    def test_should_have_downloads_folder_input_label_and_button(self):
        self.assertIsNotNone(self.ui.dlDirectPathEdit)
        self.assertIsNotNone(self.ui.dlLabel)
        self.assertEquals(self.ui.dlLabel.text(), "Downloads:")
        self.assertIsNotNone(self.ui.dlSearchBtn)

    def test_should_have_destination_folder_input_label_and_button(self):
        self.assertIsNotNone(self.ui.destPathEdit)
        self.assertIsNotNone(self.ui.destLabel)
        self.assertEquals(self.ui.destLabel.text(), "Destination:")
        self.assertIsNotNone(self.ui.destSearchBtn)

#     TODO: add test that ensures path on view is not replaced on file dialog close


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(SettingsPageTest)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()
