import utility

def scan_library(directory: str):
    if utility.does_file_exist(directory):
        directory_map = utility.map_folder_and_subfolders(directory)
        # flatten directory map?
        # add each file as `AudioFile` type
        # add artists and genres to working db
