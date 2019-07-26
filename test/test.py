# Author: Jacques Mathieu
# Created on 6/13/2019 at 1:51 AM
# Part of the AudioFileManager project
# Main testing file

import utility as util
import config
import sys

# Test's global variables
TESTS_PASSED = 0
TESTS_FAILED = 0


# Compare results of conducted test
def compare_results(expected, actual, name):
    global TESTS_PASSED
    global TESTS_FAILED
    # Allow for testing of multiple possible expected outcomes
    if type(expected) is dict and "pos_outcomes" in expected.keys():
        possible_outcomes = expected['pos_outcomes']
        prev_tests_passed = TESTS_PASSED
        # Iterate through each possible outcome and see if at least one was true
        for o in possible_outcomes:
            if actual == o:
                TESTS_PASSED = TESTS_PASSED + 1
                break
        # If no change in tests passed, mark this test as a failure
        if prev_tests_passed == TESTS_PASSED:
            print("Error in " + name)
            TESTS_FAILED = TESTS_FAILED + 1
    else:
        if actual != expected:
            print("Error in " + name)
            TESTS_FAILED = TESTS_FAILED + 1
        else:
            TESTS_PASSED = TESTS_PASSED + 1


# Print all test results and stop script from running if any test failed
def print_test_results():
    global TESTS_PASSED
    global TESTS_FAILED
    print(str(TESTS_PASSED) + " successful test(s) and " + str(TESTS_FAILED) +
          " failed test(s).\n--------------------------------------------\n")
    if TESTS_FAILED > 0:
        print("Stopping script b/c of failed tests")
        exit()


# Test some of the utility functions in the utility file
def util_funcs_test():
    test_folder_path = "test/test_folder"
    t_name_main_pre = "Utility Functions Test"

    # Test 'does_file_exist' function
    name = t_name_main_pre + ": Does path exist? [No]"
    expected = False
    actual = util.does_file_exist(test_folder_path)
    compare_results(expected, actual, name)

    name = t_name_main_pre + ": Does path exist? [Yes]"
    expected = True
    actual = util.does_file_exist("test")
    compare_results(expected, actual, name)

    # Test 'create_folder_if_dne' function
    name = t_name_main_pre + ": Create folder that DNE"
    test_folder_path = util.create_folder_if_dne(test_folder_path)
    actual = util.does_file_exist(test_folder_path)
    expected = True
    compare_results(expected, actual, name)

    # Test 'delete_empty_folder' function
    name = t_name_main_pre + ": Delete empty folder"
    util.delete_empty_folder(test_folder_path)
    actual = util.does_file_exist(test_folder_path)
    expected = False
    compare_results(expected, actual, name)

    # Test 'create_file_if_dne' function
    name = t_name_main_pre + ": Create file"
    test_fp = "test/test_file.txt"
    util.create_file_if_dne(test_fp, ["This is a test \nWow! A new line and no need for writelines()!"])
    expected = True
    actual = util.does_file_exist(test_fp)
    compare_results(expected, actual, name)

    # Test 'delete_file' function
    name = t_name_main_pre + ": Delete file"
    util.delete_file(test_fp)
    expected = False
    actual = util.does_file_exist(test_fp)
    compare_results(expected, actual, name)


# Test get config directory function
def get_config_dir_test():
    t_name_prefix = "Get Configuration Path Test"
    name = t_name_prefix + ": TEST_ACTIVE = False"
    expected = config.CONFIG_DIR
    actual = config.get_config_dir()
    compare_results(expected, actual, name)

    config.TEST_ACTIVE = True
    name = t_name_prefix + ": TEST_ACTIVE = True"
    expected = config.TEST_CONFIG_DIR
    actual = config.get_config_dir()
    compare_results(expected, actual, name)

    # Return config module to its default state
    config.TEST_ACTIVE = False
    config.CONFIG_JSON = {}


# Perform test on config_status() function in config.py
def config_status_test():
    t_name_prefix = "Configuration JSON file Status Check Test"
    # Enable test mode
    config.TEST_ACTIVE = True

    # Test status checker with no file in test config path
    name = t_name_prefix + ": File not found"
    actual = config.config_status()
    expected = "DNE"
    compare_results(expected, actual, name)

    # Test status checker with template file in test config path
    name = t_name_prefix + ": Create New Template File"
    # Make the config file
    config.create_config_file()
    actual = config.config_status()
    expected = "template"
    compare_results(expected, actual, name)

    # Make test folders which will be used in setting up our config file
    test_dl_folder = util.create_folder_if_dne("test/test_downloads")
    test_edit_folder = util.create_folder_if_dne("test/test_edit")
    test_final_folder = util.create_folder_if_dne("test/test_final")

    # Test 'set_downloads_folder' function
    name = t_name_prefix + ": Setting downloads folder"
    config.set_downloads_folder(test_dl_folder)
    expected = test_dl_folder
    actual = config.get_downloads_folder()
    compare_results(expected, actual, name)

    name = t_name_prefix + ": Setting downloads folder [2]"
    config.set_downloads_folder("This Should Not Overwrite")
    expected = test_dl_folder
    actual = config.get_downloads_folder()
    compare_results(expected, actual, name)

    # Test 'update_downloads_folder' function
    name = t_name_prefix + ": Update downloads folder"
    config.update_downloads_folder("This Should Overwrite")
    expected = "This Should Overwrite"
    actual = config.get_downloads_folder()
    compare_results(expected, actual, name)

    # Test 'config_status' with one item filled out (and correctly)
    name = t_name_prefix + ": 1/3 with one bogus entry at pos 1"
    expected = "path_dne"
    actual = config.config_status()
    compare_results(expected, actual, name)

    # Test 'update_downloads_folder' function (again)
    name = t_name_prefix + ": Update downloads folder [2]"
    config.update_downloads_folder(test_dl_folder)
    expected = test_dl_folder
    actual = config.get_downloads_folder()
    compare_results(expected, actual, name)

    # Test 'config_status' with one item filled out (and correctly)
    name = t_name_prefix + ": 1/3 Complete"
    expected = "incomplete"
    actual = config.config_status()
    compare_results(expected, actual, name)

    # Test 'set_editing_folder' function
    name = t_name_prefix + ": Setting editing folder"
    config.set_editing_folder(test_edit_folder)
    expected = test_edit_folder
    actual = config.get_editing_folder()
    compare_results(expected, actual, name)

    name = t_name_prefix + ": Setting editing folder [2]"
    config.set_editing_folder("This Should Not Overwrite")
    expected = test_edit_folder
    actual = config.get_editing_folder()
    compare_results(expected, actual, name)

    # Test 'update_editing_folder' function
    name = t_name_prefix + ": Update editing folder"
    config.update_editing_folder("This Should Overwrite")
    expected = "This Should Overwrite"
    actual = config.get_editing_folder()
    compare_results(expected, actual, name)

    # Test 'config_status' with one item filled out (and correctly)
    name = t_name_prefix + ": 2/3 with one bogus entry at pos 2"
    expected = "path_dne"
    actual = config.config_status()
    compare_results(expected, actual, name)

    # Test 'update_editing_folder' function (again)
    name = t_name_prefix + ": Update editing folder [2]"
    config.update_editing_folder(test_edit_folder)
    expected = test_edit_folder
    actual = config.get_editing_folder()
    compare_results(expected, actual, name)

    # Test 'config_status' with 2 items filled out
    name = t_name_prefix + ": 2/3 Complete"
    expected = "incomplete"
    actual = config.config_status()
    compare_results(expected, actual, name)

    # Test 'set_destination_folder' function
    name = t_name_prefix + ": Setting destination folder"
    config.set_destination_folder(test_final_folder)
    expected = test_final_folder
    actual = config.get_destination_folder()
    compare_results(expected, actual, name)

    name = t_name_prefix + ": Setting destination folder [2]"
    config.set_destination_folder("This Should Not Overwrite")
    expected = test_final_folder
    actual = config.get_destination_folder()
    compare_results(expected, actual, name)

    # Test 'update_editing_folder' function
    name = t_name_prefix + ": Update destination folder"
    config.update_destination_folder("This Should Overwrite")
    expected = "This Should Overwrite"
    actual = config.get_destination_folder()
    compare_results(expected, actual, name)

    # Test 'config_status' with one item filled out (and correctly)
    name = t_name_prefix + ": 3/3 with one bogus entry at pos 3"
    expected = "path_dne"
    actual = config.config_status()
    compare_results(expected, actual, name)

    # Test 'update_editing_folder' function (again)
    name = t_name_prefix + ": Update destination folder [2]"
    config.update_destination_folder(test_final_folder)
    expected = test_final_folder
    actual = config.get_destination_folder()
    compare_results(expected, actual, name)

    # Test 'config_status' with everything filled out and existent
    name = t_name_prefix + ": Completed Config File"
    expected = "complete"
    actual = config.config_status()
    compare_results(expected, actual, name)

    # Return config module to its default state
    config.TEST_ACTIVE = False
    config.CONFIG_JSON = {}
    util.delete_file(config.TEST_CONFIG_DIR)
    # Delete temp files
    util.delete_empty_folder(test_dl_folder)
    util.delete_empty_folder(test_edit_folder)
    util.delete_empty_folder(test_final_folder)


# Run all tests
def test_all():
    util_funcs_test()
    get_config_dir_test()
    config_status_test()
    print_test_results()
