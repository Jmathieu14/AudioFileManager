# Author: Jacques Mathieu
# Created on 1/8/2020 at 9:40 PM
# Part of the AudioFileManager project

from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import sys
import unittest
import settings_gui

test_app = QApplication(sys.argv)

class SettingsPageTest(unittest.TestCase):

    def setUp(self):
        self.settings_page = settings_gui.SettingsView()

    def test_should_have_title(self):
        self.assertEquals(self.settings_page.ui.settings, "settings")


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(SettingsPageTest)


def main():
    unittest.TextTestRunner().run(get_suite())


if __name__ == '__main__':
    unittest.main()
