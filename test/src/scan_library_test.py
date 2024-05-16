import unittest
from unittest import mock

from src.functions.scan_library import audio_file_to_artist, get_genre_from_audio_file
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
    def test_creates_genre_and_adds_to_db(self, audio_file_mock):
        database.init_database_object()
        audio_file_mock.metadata = constants.solo_skrillex_audio_file
        actual_genre = get_genre_from_audio_file(audio_file_mock)
        self.assertEqual(audio_file_mock.metadata["genre"], actual_genre.name)
        self.assertTrue(
            actual_genre.__eq__(database.find_item_by_name(actual_genre.name))
        )


class AudioFileToArtistTest(unittest.TestCase):
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
        actual_artist = audio_file_to_artist(None, [])
        self.assertIsNone(actual_artist)

    @mock.patch("src.models.audio_file")
    def test_returns_none_if_metadata_is_none(self, audio_file_mock):
        audio_file_mock.metadata = None
        actual_artist = audio_file_to_artist(audio_file_mock, [])
        self.assertIsNone(actual_artist)

    @mock.patch("src.models.audio_file")
    def test_returns_none_if_audio_file_artist_is_none(self, audio_file_mock):
        audio_file_mock.metadata = {"artist": None}
        actual_artist = audio_file_to_artist(audio_file_mock, [])
        self.assertIsNone(actual_artist)

    @mock.patch("src.models.audio_file")
    def test_returns_none_if_audio_file_artist_is_empty_string(self, audio_file_mock):
        audio_file_mock.metadata = {"artist": ""}
        actual_artist = audio_file_to_artist(audio_file_mock, [])
        self.assertIsNone(actual_artist)

    @mock.patch("src.models.audio_file")
    def test_creates_single_artist(self, audio_file_mock):
        database.init_database_object()
        database.save_item_to_database_if_does_not_exist(constants.existing_genre)
        audio_file_mock.metadata = constants.solo_skrillex_audio_file
        expected_artist_name = "Skrillex"
        expected_genres_list = [constants.existing_genre.id]
        actual_artist = audio_file_to_artist(audio_file_mock, [])
        self.assertEqual(expected_artist_name, actual_artist.name)
        self.assertEqual(expected_genres_list, actual_artist.genres)


def main():
    genre_from_audio_file_suite = unittest.TestLoader().loadTestsFromTestCase(
        GetGenreFromAudioFileTest
    )
    audio_file_to_artist_suite = unittest.TestLoader().loadTestsFromTestCase(
        AudioFileToArtistTest
    )
    unittest.TextTestRunner().run(genre_from_audio_file_suite)
    unittest.TextTestRunner().run(audio_file_to_artist_suite)


if __name__ == "__main__":
    unittest.main()
