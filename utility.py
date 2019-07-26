# Author: Jacques Mathieu
# Created on 6/13/2019 at 1:53 AM
# Part of the AudioFileManager project

# Utility functions file
# Jacques Mathieu - 11/4/18 [Copied from StorageOptimizer project]

import os.path as osp
import os
import simplejson as j


# Make a file given the content and path (where text is a list of str)
def create_file_if_dne(path, text):
    if not path.__str__().find(osp.curdir.__str__()):
        path = osp.abspath(osp.curdir + "\\" + path)
    if not osp.exists(path):
        f = open(path, "w")
        f.writelines(text)
        f.close()
    return path


# Create folder if it does not yet exist. Return the file path created
# See Source 1 for aid with this function (bottom of page)
def create_folder_if_dne(folder_name):
    full_path = osp.abspath(osp.curdir + "\\" + folder_name)
    if not osp.exists(full_path):
        os.makedirs(full_path)
    return full_path


# Delete a file given its path
def delete_file(path):
    if not path.__str__().find(osp.curdir.__str__()):
        path = osp.abspath(osp.curdir + "\\" + path)
    if osp.exists(path):
        os.remove(path)


# Remove EMPTY folder given its path
def delete_empty_folder(path):
    if not path.__str__().find(osp.curdir.__str__()):
        path = osp.abspath(osp.curdir + "\\" + path)
    os.rmdir(path)


# Return True if file exists, else return False
def does_file_exist(path):
    if not path.__str__().find(osp.curdir.__str__()):
        path = osp.abspath(osp.curdir + "\\" + path)
    return osp.exists(path)


# Attempt conversion of string, return string version if cannot be converted to int
# See source 2 for more info
def tryint(s):
    try:
        return int(s)
    except ValueError:
        return s


# Convert hex string to base10 string
def hex_to_base10_string(hex):
    idxs_to_replace = []
    new_vals = []
    ctr = 0
    for c in hex:
        new_val = -1
        if c == 'a':
            new_val = 10
        elif c == 'b':
            new_val = 11
        elif c == 'c':
            new_val = 12
        elif c == 'd':
            new_val = 13
        elif c == 'e':
            new_val = 14
        elif c == 'f':
            new_val = 15

        if new_val != -1:
            new_vals.append(new_val)
            idxs_to_replace.append(ctr)

        ctr = ctr + 1

    ctr = 0
    item_ct = idxs_to_replace.__len__()
    new_full_str = ""
    last_idx = 0

    for ctr in range(item_ct):
        new_str = str(new_vals[ctr])
        new_full_str += hex[last_idx:idxs_to_replace[ctr]] + new_str
        last_idx = idxs_to_replace[ctr] + 1

    # Add last part of string
    new_full_str += hex[last_idx:]

    return new_full_str


# Save json (or dict) to file
def json_to_file(my_json, filename):
    last_five_idx = filename.__len__() - 5
    last_five = filename[last_five_idx:]
    if last_five.lower() != ".json":
        filename = filename + ".json"
    filepath = osp.curdir + "\\json\\" + filename
    # If the full filepath was passed in...
    if filename.find(osp.curdir) >= 0:
        filepath = filename
    with open(filepath, 'w') as my_file:
        my_file.write(j.dumps(my_json, indent="\t"))
    return filename


# return python dict object version of a json file
def file_to_json_obj(filename):
    with open(filename, 'r') as my_file:
        s = my_file.read()
    my_in = j.loads(s)
    return my_in


# Print a dict object in a pretty manner
def pretty_print_json(my_json):
    print(j.dumps(my_json, indent="\t"))


# Return deep copy of given json
def copy_json(my_json):
    return j.loads(j.dumps(my_json))


# Helper function for map_folder_and_subfolders
def map_f_and_sf_helper(my_folder, my_folder_obj):
    if osp.exists(my_folder) and osp.isdir(my_folder):
        my_files_or_subdirs = os.listdir(my_folder)
        idx = 0
        for f_or_sd in my_files_or_subdirs:
            f_or_sd = my_folder + "\\" + f_or_sd
            if osp.isdir(f_or_sd):
                ret_val = map_folder_and_subfolders(f_or_sd)
                my_files_or_subdirs[idx] = ret_val[f_or_sd]
            else:
                my_files_or_subdirs[idx] = f_or_sd
            idx = idx + 1
        my_folder_obj[my_folder] = my_files_or_subdirs
        return my_folder_obj
    else:
        print(my_folder + " does not exist or is not a folder")


# Return a python dict containing each file name and folder path
# within a directory
def map_folder_and_subfolders(my_folder):
    my_folder_obj = {my_folder: []}
    return map_f_and_sf_helper(my_folder, my_folder_obj)


# Flatten a folder list to only contain filepaths to files (ignoring the parent folder)
def flatten_folder_list(parent, folder_list):
    print("TODO: flatten_folder_list")







# Source 1:
# https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python
# Blair Conrad's answer

# Source 2:
# http://stupidpythonideas.blogspot.com/2015/05/how-to-detect-valid-integer-literal.html
# How to convert to int without crashing program :)
