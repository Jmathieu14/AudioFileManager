import unittest
from unittest import mock

from tinydb import Query
from src.functions.scan_library import audio_file_to_artist
from src.models.artist import Artist
import utility as util
import config
import src.functions.database as database
import test.test_constants as constants


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
        audio_file_mock.metadata = {'artist': None}
        actual_artist = audio_file_to_artist(audio_file_mock, [])
        self.assertIsNone(actual_artist)

    @mock.patch("src.models.audio_file")
    def test_returns_none_if_audio_file_artist_is_empty_string(self, audio_file_mock):
        audio_file_mock.metadata = {'artist': ''}
        actual_artist = audio_file_to_artist(audio_file_mock, [])
        self.assertIsNone(actual_artist)

    @mock.patch("src.models.audio_file")
    def test_creates_single_artist(self, audio_file_mock):
        database.init_database_object()
        database.save_item_to_database_if_does_not_exist(constants.existing_genre)
        audio_file_mock.metadata = constants.solo_skrillex_audio_file
        expected_artist_name = 'Skrillex'
        expected_genres_list = [constants.existing_genre.id]
        actual_artist = audio_file_to_artist(audio_file_mock, [])
        self.assertEqual(expected_artist_name, actual_artist.name)
        self.assertEqual(expected_genres_list, actual_artist.genres)


def main():
    audio_file_to_artist_suite = unittest.TestLoader(
    ).loadTestsFromTestCase(AudioFileToArtistTest)
    unittest.TextTestRunner().run(audio_file_to_artist_suite)


if __name__ == '__main__':
    unittest.main()
