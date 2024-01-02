from src.models.audio_file import AudioFile
import utility
import os.path as osp


audio_file_extensions = utility.file_to_json_obj(osp.abspath("../../ext/audio_codecs.json"))

def scan_library(directory: str):
    if utility.does_file_exist(directory):
        flattened_file_list = utility.flatten_folder(directory)
        audio_files = []
        for filepath in flattened_file_list:
            if osp.splitext(filepath) in audio_file_extensions:
                audio_file = AudioFile(filepath)
                audio_files.append(audio_file)
    for audio_file in audio_files:
        print(audio_file.metadata)
