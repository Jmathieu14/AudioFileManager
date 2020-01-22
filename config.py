# Author: Jacques Mathieu
# Created on 6/13/2019 at 2:03 AM
# Part of the AudioFileManager project
# Program that sets up configuration file for user

import utility as util

CONFIG_DIRECTORY = "config"
CONFIG_FILE_PATH = "config/config.json"
# Make sure test module can access the test config file
TEST_CONFIG_FILE_PATH = "./config/test_config.json"
TEST_CONFIG_DIRECTORY = "./config"
TEST_ACTIVE = False
CONFIG_JSON = {}

# Template for the configuration file
config_template = {
  "downloads-folder": "",
  "editing-folder": "",
  "destination-folder": ""
}


# Returns correct config file path based on TEST_ACTIVE value
def get_config_file_path():
    if TEST_ACTIVE:
        return TEST_CONFIG_FILE_PATH
    else:
        return CONFIG_FILE_PATH


# Returns correct config directory path based on TEST_ACTIVE value
def get_config_directory():
    if TEST_ACTIVE:
        return TEST_CONFIG_DIRECTORY
    else:
        return CONFIG_DIRECTORY


# Print the current mode the config.py file is in
def print_mode():
    if TEST_ACTIVE:
        print("Test Mode Active")
    else:
        print("Live Mode Active")


# Initialize config
def init_config():
    status = config_status()
    if status == "DNE" or status == "empty":
        create_config_file()
        print("Updated status of configuration: " + config_status())


# Save the config file
def save_config():
    my_config_file_path = get_config_file_path()
    util.json_to_file(CONFIG_JSON, my_config_file_path)


# Return status of config file
def config_status():
    global CONFIG_JSON
    my_config_file_path = get_config_file_path()
    # Does the file exist?
    if not util.does_file_exist(my_config_file_path):
        return "DNE"
    else:
        CONFIG_JSON = util.file_to_json_obj(my_config_file_path)
        # If file is empty, return empty
        if CONFIG_JSON == None or CONFIG_JSON == {} or CONFIG_JSON == "":
            return "empty"
        # If file matches the template, return template
        elif CONFIG_JSON == config_template:
            return "template"
    my_keys = CONFIG_JSON.keys()
    for k in my_keys:
        # If at least one path is missing, return incomplete status
        if CONFIG_JSON[k] is None or CONFIG_JSON[k] == "":
            return "incomplete"
        # If folder does not exist, return 'path_dne' status
        elif not util.does_file_exist(CONFIG_JSON[k]):
            return "path_dne"
    # If we get all the way here, then everything checks out
    return "complete"


# Make a config file using the config template
def create_config_file():
    status = config_status()
    # Only do so if file truly does not exist
    if status == "DNE" or status == "empty":
        my_config_directory = get_config_directory()
        util.create_folder_if_dne(my_config_directory)
        my_config_file_path = get_config_file_path()
        util.json_to_file(config_template, my_config_file_path)
        # Make sure we are accessing the global version of CONFIG_JSON; See bottom of page for info on this (Source 1)
        global CONFIG_JSON
        CONFIG_JSON = util.file_to_json_obj(my_config_file_path)


# Set the downloads folder path for our config file
def set_downloads_folder(path):
    global CONFIG_JSON
    if "downloads-folder" in CONFIG_JSON.keys():
        if CONFIG_JSON["downloads-folder"] == "":
            CONFIG_JSON["downloads-folder"] = path
            save_config()


# Update the downloads folder path for our config file
def update_downloads_folder(path):
    global CONFIG_JSON
    if "downloads-folder" in CONFIG_JSON.keys():
        CONFIG_JSON["downloads-folder"] = path
        save_config()


# Get the path for the configured downloads folder
def get_downloads_folder():
    if "downloads-folder" in CONFIG_JSON.keys():
        return CONFIG_JSON["downloads-folder"]


# Set the editing folder path for our config file
def set_editing_folder(path):
    global CONFIG_JSON
    if "editing-folder" in CONFIG_JSON.keys():
        if CONFIG_JSON["editing-folder"] == "":
            CONFIG_JSON["editing-folder"] = path
            save_config()


# Update the editing folder path for our config file
def update_editing_folder(path):
    global CONFIG_JSON
    if "editing-folder" in CONFIG_JSON.keys():
        CONFIG_JSON["editing-folder"] = path
        save_config()


# Get the path for the configured editing folder
def get_editing_folder():
    if "editing-folder" in CONFIG_JSON.keys():
        return CONFIG_JSON["editing-folder"]


# Set the destination folder path for our config file
def set_destination_folder(path):
    global CONFIG_JSON
    if "destination-folder" in CONFIG_JSON.keys():
        if CONFIG_JSON["destination-folder"] == "":
            CONFIG_JSON["destination-folder"] = path
            save_config()


# Update the destination folder path for our config file
def update_destination_folder(path):
    global CONFIG_JSON
    if "destination-folder" in CONFIG_JSON.keys():
        CONFIG_JSON["destination-folder"] = path
        save_config()


# Get the path for the configured destination folder
def get_destination_folder():
    if "destination-folder" in CONFIG_JSON.keys():
        return CONFIG_JSON["destination-folder"]


# Setup config file for user
def setup_config_file():
    return None


# Run this to initialize config file. Must be run AFTER tests have been called in main.py file
def main():
    # Print the mode the config file is being run in
    print_mode()
    # Show config.py's status
    print("Status of configuration: " + config_status())
    # Initialize config if not already done
    init_config()


# Source 1: Help on using global variables within the same module
# https://stackoverflow.com/questions/7060711/accessing-module-level-variables-from-within-a-function-in-the-module
