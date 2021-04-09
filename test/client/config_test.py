import utility as util
import config
from test import test_util


# Test get config directory function
def get_config_dir_test():
    t_name_prefix = "Get Configuration Path Test"
    name = t_name_prefix + ": TEST_ACTIVE = False"
    expected = config.CONFIG_FILE_PATH
    actual = config.get_config_file_path()
    test_util.compare_results(expected, actual, name)

    config.TEST_ACTIVE = True
    name = t_name_prefix + ": TEST_ACTIVE = True"
    expected = config.TEST_CONFIG_FILE_PATH
    actual = config.get_config_file_path()
    test_util.compare_results(expected, actual, name)

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
    test_util.compare_results(expected, actual, name)

    # Test status checker with template file in test config path
    name = t_name_prefix + ": Create New Template File"
    # Make the config file
    config.create_config_file()
    actual = config.config_status()
    expected = "template"
    test_util.compare_results(expected, actual, name)

    # Make test folders which will be used in setting up our config file
    test_dl_folder = util.create_folder_if_dne("test/test_downloads")
    test_edit_folder = util.create_folder_if_dne("test/test_edit")
    test_final_folder = util.create_folder_if_dne("test/test_final")

    # Test 'set_downloads_folder' function
    name = t_name_prefix + ": Setting downloads folder"
    config.set_downloads_folder(test_dl_folder)
    expected = test_dl_folder
    actual = config.get_downloads_folder()
    test_util.compare_results(expected, actual, name)

    name = t_name_prefix + ": Setting downloads folder [2]"
    config.set_downloads_folder("This Should Not Overwrite")
    expected = test_dl_folder
    actual = config.get_downloads_folder()
    test_util.compare_results(expected, actual, name)

    # Test 'update_downloads_folder' function
    name = t_name_prefix + ": Update downloads folder"
    config.update_downloads_folder("This Should Overwrite")
    expected = "This Should Overwrite"
    actual = config.get_downloads_folder()
    test_util.compare_results(expected, actual, name)

    # Test 'config_status' with one item filled out (and correctly)
    name = t_name_prefix + ": 1/3 with one bogus entry at pos 1"
    expected = "path_dne"
    actual = config.config_status()
    test_util.compare_results(expected, actual, name)

    # Test 'update_downloads_folder' function (again)
    name = t_name_prefix + ": Update downloads folder [2]"
    config.update_downloads_folder(test_dl_folder)
    expected = test_dl_folder
    actual = config.get_downloads_folder()
    test_util.compare_results(expected, actual, name)

    # Test 'config_status' with one item filled out (and correctly)
    name = t_name_prefix + ": 1/3 Complete"
    expected = "incomplete"
    actual = config.config_status()
    test_util.compare_results(expected, actual, name)

    # Test 'set_editing_folder' function
    name = t_name_prefix + ": Setting editing folder"
    config.set_editing_folder(test_edit_folder)
    expected = test_edit_folder
    actual = config.get_editing_folder()
    test_util.compare_results(expected, actual, name)

    name = t_name_prefix + ": Setting editing folder [2]"
    config.set_editing_folder("This Should Not Overwrite")
    expected = test_edit_folder
    actual = config.get_editing_folder()
    test_util.compare_results(expected, actual, name)

    # Test 'update_editing_folder' function
    name = t_name_prefix + ": Update editing folder"
    config.update_editing_folder("This Should Overwrite")
    expected = "This Should Overwrite"
    actual = config.get_editing_folder()
    test_util.compare_results(expected, actual, name)

    # Test 'config_status' with one item filled out (and correctly)
    name = t_name_prefix + ": 2/3 with one bogus entry at pos 2"
    expected = "path_dne"
    actual = config.config_status()
    test_util.compare_results(expected, actual, name)

    # Test 'update_editing_folder' function (again)
    name = t_name_prefix + ": Update editing folder [2]"
    config.update_editing_folder(test_edit_folder)
    expected = test_edit_folder
    actual = config.get_editing_folder()
    test_util.compare_results(expected, actual, name)

    # Test 'config_status' with 2 items filled out
    name = t_name_prefix + ": 2/3 Complete"
    expected = "incomplete"
    actual = config.config_status()
    test_util.compare_results(expected, actual, name)

    # Test 'set_destination_folder' function
    name = t_name_prefix + ": Setting destination folder"
    config.set_destination_folder(test_final_folder)
    expected = test_final_folder
    actual = config.get_destination_folder()
    test_util.compare_results(expected, actual, name)

    name = t_name_prefix + ": Setting destination folder [2]"
    config.set_destination_folder("This Should Not Overwrite")
    expected = test_final_folder
    actual = config.get_destination_folder()
    test_util.compare_results(expected, actual, name)

    # Test 'update_editing_folder' function
    name = t_name_prefix + ": Update destination folder"
    config.update_destination_folder("This Should Overwrite")
    expected = "This Should Overwrite"
    actual = config.get_destination_folder()
    test_util.compare_results(expected, actual, name)

    # Test 'config_status' with one item filled out (and correctly)
    name = t_name_prefix + ": 3/3 with one bogus entry at pos 3"
    expected = "path_dne"
    actual = config.config_status()
    test_util.compare_results(expected, actual, name)

    # Test 'update_editing_folder' function (again)
    name = t_name_prefix + ": Update destination folder [2]"
    config.update_destination_folder(test_final_folder)
    expected = test_final_folder
    actual = config.get_destination_folder()
    test_util.compare_results(expected, actual, name)

    # Test 'config_status' with everything filled out and existent
    name = t_name_prefix + ": Completed Config File"
    expected = "complete"
    actual = config.config_status()
    test_util.compare_results(expected, actual, name)

    # Return config module to its default state
    config.TEST_ACTIVE = False
    config.CONFIG_JSON = {}
    util.delete_file(config.TEST_CONFIG_FILE_PATH)
    # Delete temp files
    util.delete_empty_folder(test_dl_folder)
    util.delete_empty_folder(test_edit_folder)
    util.delete_empty_folder(test_final_folder)

def main():
    get_config_dir_test()
    config_status_test()

if __name__ == '__main__':
    main()
