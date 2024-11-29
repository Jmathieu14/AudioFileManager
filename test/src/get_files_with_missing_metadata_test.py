import unittest
from unittest import mock

from src.functions.scan_library import audio_file_to_artists, get_genre_from_audio_file
import utility as util
import config
import src.functions.database as database
import test.test_constants as constants


class GetFilesWithMissingMetadataTest(unittest.TestCase):
    def setUp(self) -> None:
        config.TEST_ACTIVE = True
        config.main(debug=False)

    def tearDown(self) -> None:
        database.close_database()
        util.delete_file(config.TEST_CONFIG_FILE_PATH)
        util.delete_file(config.TEST_DATABASE_FILE_PATH)
        util.delete_empty_folder(config.TEST_CONFIG_DIRECTORY)
        config.TEST_ACTIVE = False


def main():
    get_files_with_missing_metadata_suite = unittest.TestLoader().loadTestsFromTestCase(
        GetFilesWithMissingMetadataTest
    )
    unittest.TextTestRunner().run(get_files_with_missing_metadata_suite)


if __name__ == "__main__":
    unittest.main()
