import unittest
from unittest import mock
import utility as util
import config
import src.functions.database as database
import test.test_constants as constants


class DatabaseMockTests(unittest.TestCase):
    def setUp(self) -> None:
        config.TEST_ACTIVE = True
        config.main(debug=False)

    def tearDown(self) -> None:
        util.delete_file(config.TEST_CONFIG_FILE_PATH)
        util.delete_file(config.TEST_DATABASE_FILE_PATH)
        util.delete_empty_folder(config.TEST_CONFIG_DIRECTORY)
        config.TEST_ACTIVE = False

    @mock.patch('tinydb.TinyDB.__init__')
    def test_init_database_object_creates_tinydb_instance(self, mock_tiny_db_init):
        mock_tiny_db_init.return_value = None
        database_file_path = config.get_database_file_path()
        database.init_database_object()
        mock_tiny_db_init.assert_called_once_with(database_file_path)

    @mock.patch('tinydb.TinyDB.__init__')
    def test_init_database_object_sets_initialized_true(self, mock_tiny_db_init):
        mock_tiny_db_init.return_value = None
        database.init_database_object()
        self.assertTrue(database.database_initialized)

    @mock.patch('src.functions.database.init_database_object')
    def test_get_database_calls_init_database_object(self, mock_init_db):
        mock_init_db.return_value = None
        database.local_database = None
        database.get_database()
        mock_init_db.assert_called_once()
        database.close_database()


class DatabaseTest(unittest.TestCase):
    def setUp(self) -> None:
        config.TEST_ACTIVE = True
        config.main(debug=False)

    def tearDown(self) -> None:
        database.close_database()
        util.delete_file(config.TEST_CONFIG_FILE_PATH)
        util.delete_file(config.TEST_DATABASE_FILE_PATH)
        util.delete_empty_folder(config.TEST_CONFIG_DIRECTORY)
        config.TEST_ACTIVE = False

    def test_does_item_exist_returns_false_for_nonexisting_artist(self):
        database.init_database_object()
        self.assertFalse(database.does_item_exist(constants.non_existing_artist))

    def test_does_item_exist_returns_false_for_nonexisting_genre(self):
        database.init_database_object()
        self.assertFalse(database.does_item_exist(constants.non_existing_genre))

    def test_does_item_exist_returns_true_for_existing_artist(self):
        database.init_database_object()
        my_db = database.get_database()
        my_db.insert(constants.existing_artist.to_dict())
        self.assertTrue(database.does_item_exist(constants.existing_artist))

    def test_does_item_exist_returns_true_for_existing_genre(self):
        database.init_database_object()
        my_db = database.get_database()
        my_db.insert(constants.existing_genre.to_dict())
        self.assertTrue(database.does_item_exist(constants.existing_genre))

    def test_get_item_by_uuid_for_artist(self):
        database.init_database_object()
        my_db = database.get_database()
        my_db.insert(constants.existing_artist.to_dict())
        my_db.insert(constants.existing_genre.to_dict())
        item = database.get_item_by_uuid(constants.existing_artist.id)
        self.assertEqual(constants.existing_artist, item)

    def test_get_item_by_uuid_for_genre(self):
        database.init_database_object()
        my_db = database.get_database()
        my_db.insert(constants.existing_artist.to_dict())
        my_db.insert(constants.existing_genre.to_dict())
        item = database.get_item_by_uuid(constants.existing_genre.id)
        self.assertEqual(constants.existing_genre, item)


def main():
    database_mock_suite = unittest.TestLoader().loadTestsFromTestCase(DatabaseMockTests)
    database_suite = unittest.TestLoader().loadTestsFromTestCase(DatabaseTest)
    unittest.TextTestRunner().run(database_mock_suite)
    unittest.TextTestRunner().run(database_suite)


if __name__ == '__main__':
    unittest.main()