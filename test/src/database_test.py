import uuid
from tinydb import Query, TinyDB
import utility as util
from test import test_util
import config
import src.functions.database as database


def startup():
    config.TEST_ACTIVE = True
    config.main()


def teardown():
    util.delete_file(config.TEST_CONFIG_FILE_PATH)
    util.delete_file(config.TEST_DATABASE_FILE_PATH)
    util.delete_empty_folder(config.TEST_CONFIG_DIRECTORY)
    config.TEST_ACTIVE = False


def init_database_object_test():
    startup()
    t_name_prefix = "Init Database Object Test"
    
    name = t_name_prefix + ": Should create TinyDB object"
    database_file_path = config.get_database_file_path()
    expected_database_object = TinyDB(database_file_path)
    test_record_uuid = uuid.uuid4().__str__()
    expected_database_object.insert({"id": test_record_uuid})
    database.init_database_object()
    actual_database_object = database.get_database()
    q = Query()
    test_util.compare_results(expected=expected_database_object.search(q.id == test_record_uuid),
                              actual=actual_database_object.search(q.id == test_record_uuid),
                              name=name)
    actual_database_object.close()
    expected_database_object.close()
    
    teardown()


def main():
    init_database_object_test()


if __name__ == '__main__':
    main()