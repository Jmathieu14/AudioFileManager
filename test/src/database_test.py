import unittest
from unittest import mock

from tinydb import Query
from src.models.artist import Artist
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

    def test_find_item_by_name_returns_item_based_on_name(self):
        database.init_database_object()
        my_db = database.get_database()
        my_db.insert(constants.existing_artist.to_dict())
        actual_item = database.find_item_by_name("skrillex")
        self.assertEqual(constants.existing_artist, actual_item)

    def test_find_item_by_name_does_not_return_item_based_on_bad_name_casing(self):
        database.init_database_object()
        my_db = database.get_database()
        my_db.insert(constants.existing_artist.to_dict())
        actual_item = database.find_item_by_name("skrillex", ignore_case=False)
        self.assertEqual(None, actual_item)

    def test_find_item_by_name_returns_item_based_on_aka_name(self):
        database.init_database_object()
        my_db = database.get_database()
        my_db.insert(constants.existing_artist.to_dict())
        actual_item = database.find_item_by_name("SOnny moore")
        self.assertEqual(constants.existing_artist, actual_item)

    def test_find_item_by_name_does_not_return_item_based_on_bad_aka_name_casing(self):
        database.init_database_object()
        my_db = database.get_database()
        my_db.insert(constants.existing_artist.to_dict())
        actual_item = database.find_item_by_name("SOnny moore", ignore_case=False)
        self.assertEqual(None, actual_item)

    def test_find_item_by_name_works_for_genre_good_casing(self):
        database.init_database_object()
        my_db = database.get_database()
        my_db.insert(constants.existing_genre.to_dict())
        actual_item = database.find_item_by_name("Dubstep", ignore_case=False)
        self.assertEqual(constants.existing_genre, actual_item)

    def test_find_item_by_name_works_for_genre_aka_good_casing(self):
        database.init_database_object()
        my_db = database.get_database()
        my_db.insert(constants.existing_genre.to_dict())
        actual_item = database.find_item_by_name("dubsteppa", ignore_case=False)
        self.assertEqual(constants.existing_genre, actual_item)

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

    def test_does_item_exist_returns_true_for_duplicate_artist(self):
        database.init_database_object()
        my_db = database.get_database()
        my_db.insert(constants.existing_artist.to_dict())
        self.assertTrue(database.does_item_exist(constants.duplicate_artist))

    def test_does_item_exist_returns_true_for_similar_artist(self):
        database.init_database_object()
        my_db = database.get_database()
        my_db.insert(constants.existing_artist.to_dict())
        self.assertTrue(database.does_item_exist(constants.similar_artist))

    def test_does_item_exist_returns_true_for_artist_with_existing_akas(self):
        database.init_database_object()
        my_db = database.get_database()
        my_db.insert(constants.existing_artist.to_dict())
        self.assertTrue(database.does_item_exist(constants.artist_with_existing_akas))

    def test_save_item_to_database_if_does_not_exist_adds_item_to_db(self):
        database.init_database_object()
        database.save_item_to_database_if_does_not_exist(constants.existing_artist)
        self.assertEqual(constants.existing_artist, database.get_item_by_uuid(constants.existing_artist.id))

    def test_save_item_to_database_if_does_not_exist_does_not_add_identical_item_to_db(self):
        database.init_database_object()
        database.save_item_to_database_if_does_not_exist(constants.existing_artist)
        database.save_item_to_database_if_does_not_exist(constants.existing_artist)
        q = Query()
        items = database.get_database().search(q.name == constants.existing_artist.name)
        self.assertEqual(1, items.__len__())
        self.assertEqual(constants.existing_artist, database.get_item_by_uuid(constants.existing_artist.id))

    def test_save_item_to_database_if_does_not_exist_does_not_add_duplicate_item_with_different_id(self):
        database.init_database_object()
        database.save_item_to_database_if_does_not_exist(constants.existing_artist)
        database.save_item_to_database_if_does_not_exist(constants.duplicate_artist)
        self.assertIsNone(database.get_item_by_uuid(constants.duplicate_artist.id))
        self.assertIsNotNone(database.get_item_by_uuid(constants.existing_artist.id))

    def test_save_item_to_database_if_does_not_exist_does_not_add_similar_item(self):
        database.init_database_object()
        database.save_item_to_database_if_does_not_exist(constants.existing_artist)
        database.save_item_to_database_if_does_not_exist(constants.similar_artist)
        self.assertIsNone(database.get_item_by_uuid(constants.similar_artist.id))
        self.assertIsNotNone(database.get_item_by_uuid(constants.existing_artist.id))


def main():
    database_mock_suite = unittest.TestLoader().loadTestsFromTestCase(DatabaseMockTests)
    database_suite = unittest.TestLoader().loadTestsFromTestCase(DatabaseTest)
    unittest.TextTestRunner().run(database_mock_suite)
    unittest.TextTestRunner().run(database_suite)


if __name__ == '__main__':
    unittest.main()