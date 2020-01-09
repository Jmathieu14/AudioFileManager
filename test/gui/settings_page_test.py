# Author: Jacques Mathieu
# Created on 1/8/2020 at 9:40 PM
# Part of the AudioFileManager project

import test.test_util as test_util
import settings_gui
import gui


def init_gui():
    gui.init()
    gui.MY_WINDOW = settings_gui.run_gui()

def quit_gui():
    gui.gui_exit()

def settings_layout_test():
    # Start gui before testing
    # init_gui()

    base_name = "Settings layout test: "
    cur_test_name = base_name + "should have downloads folder input"

    # test_util.assert_not_null(gui.get_widget("dlDirectPathEdit"), cur_test_name)

    # quit_gui()

def main():
    settings_layout_test()

if __name__ == '__main__':
    main()
