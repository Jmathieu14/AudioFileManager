import os.path as osp
from typing import List

from config import get_required_metadata, init_config
from src.functions.audio_file_util import get_audio_files_from_directory
from src.models.audio_file import AudioFile
from src.models.audio_file_missing_metadata import AudioFileMissingMetadata


init_config(debug=False)


def get_files_with_missing_metadata(directory: str) -> List[AudioFileMissingMetadata]:
    required_fields = get_required_metadata()
    print("Required fields configured by user: " + str(required_fields))
    audio_files_with_missing_metadata = []
    audio_files = get_audio_files_from_directory(directory)
    for audio_file in audio_files:
        potential_audio_file_with_missing_fields = AudioFileMissingMetadata(audio_file)
        for required_field in required_fields:
            required_field_value = audio_file.metadata[required_field]
            if required_field_value is None or str(required_field_value).strip() == "":
                potential_audio_file_with_missing_fields.add_missing_field(
                    required_field
                )
        if potential_audio_file_with_missing_fields.missing_fields.__len__() > 0:
            audio_files_with_missing_metadata.append(
                potential_audio_file_with_missing_fields
            )
    return audio_files_with_missing_metadata


def print_missing_metadata(files_with_missing_metadata: List[AudioFileMissingMetadata]):
    if files_with_missing_metadata is not None and files_with_missing_metadata != []:
        print()
        for file in files_with_missing_metadata:
            print(file.missing_fields_as_string())
    else:
        print("All audio files in given directory have the required metadata fields!")
