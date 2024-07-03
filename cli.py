import sys
from src.functions.get_files_with_missing_metadata import get_files_with_missing_metadata
from src.functions.scan_library import scan_library
# import webscraper.src.load_playlist_pages as browser
from config import main as init_config


if __name__ == "__main__":
    if sys.argv is not None:
        first_arg = sys.argv[1].lower().strip()
        if first_arg == 'scan':
            scan_library(sys.argv[2])
        elif first_arg == 'get_missing':
            files_with_missing_metadata = get_files_with_missing_metadata(sys.argv[2])
            if files_with_missing_metadata != []:
                print(files_with_missing_metadata)
            else:
                print("All audio files in given directory have the required metadata fields!")
        # elif first_arg == 'webscrape':
        #     browser.save_all_playlists_to_file()
        elif first_arg == 'init':
            init_config()
    else:
        print("No option selected")
