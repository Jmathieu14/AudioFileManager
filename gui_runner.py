# Author: Jacques Mathieu
# Created on 6/27/2019 at 2:16 PM
# File that runs the views for the AudioFileManager project


from PyQt5 import uic, QtWidgets
import gui as g
import settings_gui as sg
import main_gui as mg


# Initialize the gui
def run_gui():
    g.init()
    g.MY_WINDOW = mg.run_gui()
    g.gui_exit()
