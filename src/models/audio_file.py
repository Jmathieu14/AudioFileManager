from utility import get_absolute_directory_from_path, get_file_name_from_path
import os.path as osp
import music_tag


class AudioFile:
    def __init__(self, path: str) -> None:
        self.path = osp.abspath(path)
        self.directory = get_absolute_directory_from_path(path)
        self.file_name = get_file_name_from_path(path)
        self.metadata = music_tag.load_file(self.path)

    def save(self):
        self.metadata.save()
