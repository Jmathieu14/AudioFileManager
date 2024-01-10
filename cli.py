import sys
from src.functions.scan_library import scan_library


if __name__ == "__main__":
    if sys.argv is not None and sys.argv[1].lower().strip() == 'scan':
        scan_library(sys.argv[2])
    else:
        print("No option selected")
