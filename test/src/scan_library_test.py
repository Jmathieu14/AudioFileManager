import unittest
from unittest import mock

from src.functions.scan_library import audio_file_to_artists, get_genre_from_audio_file
import utility as util
import config
import src.functions.database as database
import test.test_constants as constants


class GetGenreFromAudioFileTest(unittest.TestCase):
    def setUp(self) -> None:
        config.TEST_ACTIVE = True
        config.main(debug=False)

    def tearDown(self) -> None:
        database.close_database()
        util.delete_file(config.TEST_CONFIG_FILE_PATH)
        util.delete_file(config.TEST_DATABASE_FILE_PATH)
        util.delete_empty_folder(config.TEST_CONFIG_DIRECTORY)
        config.TEST_ACTIVE = False

    def test_returns_none_if_audio_file_is_none(self):
        actual_genre = get_genre_from_audio_file(None)
        self.assertIsNone(actual_genre)

    @mock.patch("src.models.audio_file")
    def test_returns_none_if_metadata_is_none(self, audio_file_mock):
        audio_file_mock.metadata = None
        actual_genre = get_genre_from_audio_file(audio_file_mock)
        self.assertIsNone(actual_genre)

    @mock.patch("src.models.audio_file")
    def test_returns_none_if_audio_file_genre_is_none(self, audio_file_mock):
        audio_file_mock.metadata = {"genre": None}
        actual_genre = get_genre_from_audio_file(audio_file_mock)
        self.assertIsNone(actual_genre)

    @mock.patch("src.models.audio_file")
    def test_returns_none_if_audio_file_genre_is_empty_string(self, audio_file_mock):
        audio_file_mock.metadata = {"genre": ""}
        actual_genre = get_genre_from_audio_file(audio_file_mock)
        self.assertIsNone(actual_genre)

    @mock.patch("src.models.audio_file")
    def test_returns_expected_genre_from_db(self, audio_file_mock):
        database.init_database_object()
        database.save_item_to_database_if_does_not_exist(constants.existing_genre)
        audio_file_mock.metadata = constants.solo_skrillex_audio_file
        actual_genre = get_genre_from_audio_file(audio_file_mock)
        self.assertTrue(constants.existing_genre.__eq__(actual_genre))

    @mock.patch("src.models.audio_file")
    def test_returns_expected_genre_from_db_if_is_aka(self, audio_file_mock):
        database.init_database_object()
        database.save_item_to_database_if_does_not_exist(constants.existing_genre)
        audio_file_mock.metadata = constants.solo_skrillex_audio_file_with_aka_genre
        actual_genre = get_genre_from_audio_file(audio_file_mock)
        self.assertTrue(constants.existing_genre.__eq__(actual_genre))

    @mock.patch("src.models.audio_file")
    def test_creates_genre_and_adds_to_db(self, audio_file_mock):
        database.init_database_object()
        audio_file_mock.metadata = constants.solo_skrillex_audio_file
        actual_genre = get_genre_from_audio_file(audio_file_mock)
        self.assertEqual(audio_file_mock.metadata["genre"], actual_genre.name)
        self.assertTrue(
            actual_genre.__eq__(database.find_item_by_name(actual_genre.name))
        )


class AudioFileToArtistsTest(unittest.TestCase):
    def setUp(self) -> None:
        config.TEST_ACTIVE = True
        config.main(debug=False)

    def tearDown(self) -> None:
        database.close_database()
        util.delete_file(config.TEST_CONFIG_FILE_PATH)
        util.delete_file(config.TEST_DATABASE_FILE_PATH)
        util.delete_empty_folder(config.TEST_CONFIG_DIRECTORY)
        config.TEST_ACTIVE = False

    def test_returns_empty_list_if_audio_file_is_none(self):
        actual_artist_list = audio_file_to_artists(None, [])
        self.assertEquals(actual_artist_list, [])

    @mock.patch("src.models.audio_file")
    def test_returns_empty_list_if_metadata_is_none(self, audio_file_mock):
        audio_file_mock.metadata = None
        actual_artist_list = audio_file_to_artists(audio_file_mock, [])
        self.assertEquals(actual_artist_list, [])

    @mock.patch("src.models.audio_file")
    def test_returns_empty_list_if_audio_file_artist_is_none(self, audio_file_mock):
        audio_file_mock.metadata = {"artist": None}
        actual_artist_list = audio_file_to_artists(audio_file_mock, [])
        self.assertEquals(actual_artist_list, [])

    @mock.patch("src.models.audio_file")
    def test_returns_empty_list_if_audio_file_artist_is_empty_string(self, audio_file_mock):
        audio_file_mock.metadata = {"artist": ""}
        actual_artist_list = audio_file_to_artists(audio_file_mock, [])
        self.assertEquals(actual_artist_list, [])

    @mock.patch("src.models.audio_file")
    def test_creates_single_artist(self, audio_file_mock):
        database.init_database_object()
        database.save_item_to_database_if_does_not_exist(constants.existing_genre)
        audio_file_mock.metadata = constants.solo_skrillex_audio_file
        expected_artist_name = "Skrillex"
        expected_genres_list = [constants.existing_genre.id]
        actual_artist_list = audio_file_to_artists(audio_file_mock, [])
        self.assertEqual(expected_artist_name, actual_artist_list[0].name)
        self.assertEqual(expected_genres_list, actual_artist_list[0].genres)

    @mock.patch("src.models.audio_file")
    def test_matches_artist_with_ampersand(self, audio_file_mock):
        database.init_database_object()
        database.save_item_to_database_if_does_not_exist(constants.artist_with_ampersand)
        artist_with_ampersand_from_db = database.find_item_by_name(constants.artist_with_ampersand.name)
        audio_file_mock.metadata = constants.solo_camo_and_krooked_audio_file
        expected_artist_name = "Camo & Krooked"
        expected_genres_list = [constants.drum_and_bass.id]
        actual_artist_list = audio_file_to_artists(audio_file_mock, [artist_with_ampersand_from_db])
        self.assertEqual(expected_artist_name, actual_artist_list[0].name)
        self.assertEqual(expected_genres_list, actual_artist_list[0].genres)
        
    @mock.patch("src.models.audio_file")
    def test_matches_artists_with_ampersand(self, audio_file_mock):
        database.init_database_object()
        database.save_item_to_database_if_does_not_exist(constants.artist_with_ampersand)
        database.save_item_to_database_if_does_not_exist(constants.drum_and_bass)
        artist_with_ampersand_from_db = database.find_item_by_name(constants.artist_with_ampersand.name)
        audio_file_mock.metadata = constants.dual_artist_camo_and_krooked_and_tasha_baxter_audio_file
        expected_artist_name_1 = "Camo & Krooked"
        expected_artist_name_2 = "Tasha Baxter"
        expected_genres_list = [constants.drum_and_bass.id]
        actual_artist_list = audio_file_to_artists(audio_file_mock, [artist_with_ampersand_from_db])
        self.assertEqual(expected_artist_name_1, actual_artist_list[0].name)
        self.assertEqual(expected_artist_name_2, actual_artist_list[1].name)
        self.assertEqual(expected_genres_list, actual_artist_list[0].genres)
        self.assertEqual(expected_genres_list, actual_artist_list[1].genres)


def main():
    genre_from_audio_file_suite = unittest.TestLoader().loadTestsFromTestCase(
        GetGenreFromAudioFileTest
    )
    audio_file_to_artist_suite = unittest.TestLoader().loadTestsFromTestCase(
        AudioFileToArtistsTest
    )
    unittest.TextTestRunner().run(genre_from_audio_file_suite)
    unittest.TextTestRunner().run(audio_file_to_artist_suite)


if __name__ == "__main__":
    unittest.main()
