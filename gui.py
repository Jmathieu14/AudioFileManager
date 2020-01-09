# Author: Jacques Mathieu
# Created on 6/21/2019 at 5:56 PM
# Part of the AudioFileManager project

import sys

from PyQt5 import QtWidgets, QtGui

import main_gui as mg
import settings_gui as sg

MY_APP = None
MY_WINDOW = None


# Print all object names of widgets in application nicely
def pretty_print_widgets():
    widgets = get_widgets()
    for w in widgets:
        print(w.objectName())


# Populate the fields for the appropriate widgets
def populate_fields(my_vals):
    val_keys = my_vals.keys()
    if val_keys.__len__() <= 0:
        print("The passed in POP CONFIG is not a dict or has no keys. Thus, no fields will be populated...")
    widgets = get_widgets()
    for w in widgets:
        for k in val_keys:
            if my_vals[k]['obj_name'] == w.objectName():
                # Custom handling for QPushButtons
                if w.objectName().find("Btn") >= 0:
                    # Hard to automate this process with just strings and object types (for clicked property of pyqt
                    # signals)
                    handle_push_button(w, my_vals[k])
                else:
                    # Handle all other widgets
                    handle_widget_population(w, my_vals[k])


# Handle the configuration of QPushButtons
def handle_push_button(widget, specs):
    keys = specs.keys()
    for k in keys:
        if k == "click":
            widget.clicked.connect(specs[k])
        elif k == "setText":
            widget.setText(specs[k])
        elif k == "flat":
            widget.setFlat(specs[k])
        elif k == "icon":
            link_btn_to_icon(specs['obj_name'], specs[k])



# Handle the population of a widget and the specified values
def handle_widget_population(widget, value):
    fargs = value['fargs']
    if type(value['g_fname']) == list:
        print("List of functions has yet to be tested")
        # Variable that will store all modifications made to our widget
        modified_w = widget
        i = 0
        for func in value['g_fname']:
            # For specific non-callable attributes
            if func == "clicked":
                modified_w = widget.clicked
            elif i + 1 != value['g_fname'].__len__():
                modified_w = getattr(value['gmod'], func)(modified_w)
            # We are on the last chain of functions under g_fname, and need the f function values as the argument
            else:
                if fargs is None or fargs == [] or fargs == {}:
                    getattr(value['gmod'], func) \
                        (modified_w, getattr(value['fmod'], value['fname'])())
                else:
                    getattr(value['gmod'], func) \
                        (modified_w, getattr(value['fmod'], value['fname'])(fargs))
            i = i + 1

    else:
        # function f has no arguments
        if fargs is None or fargs == [] or fargs == {}:
            getattr(value['gmod'], value['g_fname']) \
                (widget, getattr(value['fmod'], value['fname'])())
        # function f has arguments
        else:
            getattr(value['gmod'], value['g_fname']) \
                (widget, getattr(value['fmod'], value['fname'])(fargs))


# Return all of the app's widgets
def get_widgets():
    return MY_APP.allWidgets()


# Return the widget with the specified object name
def get_widget(name):
    widgets = get_widgets()
    for w in widgets:
        if w.objectName() == name:
            return w
    return None


# Open folder browser for specified object
def open_folder_browser(obj_name):
    my_w = get_widget(obj_name)
    if my_w is not None:
        f_dialog = QtWidgets.QFileDialog
        my_w.setText(f_dialog.getExistingDirectory(my_w, "Select Directory"))


# Open file browser for specified object
def open_file_browser(obj_name):
    my_w = get_widget(obj_name)
    if my_w is not None:
        my_w.setText(QtWidgets.QFileDialog.getOpenFileName()[0])


# Link the specified button object to the icon at the given path
def link_btn_to_icon(obj_name, icon_path):
    my_w = get_widget(obj_name)
    my_icon = QtGui.QIcon(icon_path)
    my_w.setIcon(my_icon)


# Show the settings view
def show_settings():
    global MY_WINDOW
    MY_WINDOW = sg.run_gui()


# Show the main view
def show_main():
    global MY_WINDOW
    MY_WINDOW = mg.run_gui()


# Exit the application
def gui_exit():
    sys.exit(MY_APP.exec_())


# Initialize the application
def init():
    global MY_APP
    MY_APP = QtWidgets.QApplication(sys.argv)
