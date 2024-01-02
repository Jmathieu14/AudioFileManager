# Test some of the utility functions in the utility file
from test import test_util
import utility as util
import os.path as osp


def util_funcs_test():
    test_folder_path = "test/test_folder"
    t_name_main_pre = "Utility Functions Test"

    # Test 'does_file_exist' function
    name = t_name_main_pre + ": Does path exist? [No]"
    expected = False
    actual = util.does_file_exist(test_folder_path)
    test_util.compare_results(expected, actual, name)

    name = t_name_main_pre + ": Does path exist? [Yes]"
    expected = True
    actual = util.does_file_exist("test")
    test_util.compare_results(expected, actual, name)

    # Test 'create_folder_if_dne' function
    name = t_name_main_pre + ": Create folder that DNE"
    test_folder_path = util.create_folder_if_dne(test_folder_path)
    actual = util.does_file_exist(test_folder_path)
    expected = True
    test_util.compare_results(expected, actual, name)

    # Test 'delete_empty_folder' function
    name = t_name_main_pre + ": Delete empty folder"
    util.delete_empty_folder(test_folder_path)
    actual = util.does_file_exist(test_folder_path)
    expected = False
    test_util.compare_results(expected, actual, name)

    # Test 'create_file_if_dne' function
    name = t_name_main_pre + ": Create file"
    test_fp = "test/test_file.txt"
    util.create_file_if_dne(test_fp, ["This is a test \nWow! A new line and no need for writelines()!"])
    expected = True
    actual = util.does_file_exist(test_fp)
    test_util.compare_results(expected, actual, name)

    # Test 'delete_file' function
    name = t_name_main_pre + ": Delete file"
    util.delete_file(test_fp)
    expected = False
    actual = util.does_file_exist(test_fp)
    test_util.compare_results(expected, actual, name)

    # Test 'flatten_folder_list' function
    name = t_name_main_pre + ": Flatten Folder List"
    test_folder_two = test_folder_path + "/folder2"
    util.create_folder_if_dne(test_folder_path)
    util.create_folder_if_dne(test_folder_two)
    test_fp = test_folder_path + "/test_file.txt"
    other_test_file = test_folder_two + "/other_test_file.txt"
    util.create_file_if_dne(test_fp, ["This is a test \nWow! A new line and no need for writelines()!"])
    util.create_file_if_dne(other_test_file, ["Love this content btw; 5 stars"])

    expected = [osp.abspath(other_test_file), osp.abspath(test_fp)]
    test_folder_map = util.map_folder_and_subfolders(test_folder_path)
    print(test_folder_map)
    actual = util.flatten_folder_map(test_folder_map)
    test_util.compare_results(expected, actual, name)
    # Test cleanup
    util.delete_file(other_test_file)
    util.delete_file(test_fp)
    util.delete_empty_folder(test_folder_two)
    util.delete_empty_folder(test_folder_path)


def main():
    util_funcs_test()

if __name__ == '__main__':
    main()
