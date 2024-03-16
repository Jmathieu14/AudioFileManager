# Author: Jacques Mathieu
# Created on 6/13/2019 at 1:51 AM
# Part of the AudioFileManager project
# Main testing file

from test import test_util
from test.client import config_test, utility_test
from test.gui import settings_page_test
from test.src import database_test, scan_library_test


def main():
    # -------  Run with custom test library  -------- #
    config_test.main()
    utility_test.main()
    test_util.verbose_print_test_results()

    # -------  Run with unittest  -------- #
    print("---------------")
    print("Unittest Tests:")
    print("---------------")

    database_test.main()
    settings_page_test.main()
    scan_library_test.main()

if __name__ == '__main__':
    main()
