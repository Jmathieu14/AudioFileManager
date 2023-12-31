

from utility import get_absolute_directory_from_path, get_file_name_from_path


class Genre:
    def __init__(self, path: str, title: str, artist: str, album_artist: str,
                 album: str, album_art: str, genre: str, year: str) -> None:
        self.title = title
        self.path = path
        self.artist = artist
        self.album_artist = album_artist
        self.album = album
        self.album_art = album_art
        self.genre = genre
        self.year = year
        self.directory = get_absolute_directory_from_path(path)
        self.file_name = get_file_name_from_path(path)
