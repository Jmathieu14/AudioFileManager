from typing import List

from src.models.audio_file import AudioFile
import utility
import os.path as osp


audio_file_extensions = utility.file_to_json_obj(
    osp.abspath("./ext/audio_codecs.json")
)["extensions"]


def get_audio_files_from_directory(directory: str) -> List[AudioFile]:
    audio_files = []
    if utility.does_file_exist(directory):
        print("Scanning '{}'".format(directory))
        flattened_file_list = utility.flatten_folder(directory)
        for filepath in flattened_file_list:
            extension = osp.splitext(filepath)[1]
            if extension in audio_file_extensions:
                audio_file = AudioFile(filepath)
                audio_files.append(audio_file)
            else:
                print("'{}' is not a supported extension".format(extension))
    else:
        print("Given directory does not exist: " + directory)
    return audio_files
