# Author: Jacques Mathieu
# Created on 6/13/2019 at 1:52 AM
# Part of the AudioFileManager project
# Main file

from test import test_wrapper as t
import gui_runner as gui_r
import config


def main():
    # Run after the tests!
    config.main()
    gui_r.run_gui()


main()

# Help importing modules from sub-directories:
# http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html

# This project uses icons designed by Alexandru Stoica. It is a completely free icon pack, and can be found here:
# https://dribbble.com/shots/2888226-1800-Free-Minimal-Icon-Pack-20x20
