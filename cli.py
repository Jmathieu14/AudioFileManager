import sys
from src.functions.scan_library import scan_library
import webscraper.src.load_playlist_pages as browser
from config import main as init_config


if __name__ == "__main__":
    if sys.argv is not None:
        first_arg = sys.argv[1].lower().strip()
        if first_arg == 'scan':
            scan_library(sys.argv[2])
        elif first_arg == 'webscrape':
            browser.save_all_playlists_to_file()
        elif first_arg == 'init':
            init_config()
    else:
        print("No option selected")
