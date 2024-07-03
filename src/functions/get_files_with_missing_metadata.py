import os.path as osp
from typing import List

from src.functions.audio_file_util import get_audio_files_from_directory
from src.models.audio_file import AudioFile


REQUIRED_FIELDS = ["artist", "albumartist", "genre", "year", "title", "album"]


# def class audio_file_with_missing_fields
# contains audio file path
# missing required fields
# contents of non-missing required fields


def get_files_with_missing_metadata(directory: str) -> List[AudioFile]:
    audio_files_with_missing_metadata = []
    audio_files = get_audio_files_from_directory(directory)
    for audio_file in audio_files:
        for required_field in REQUIRED_FIELDS:
            required_field_value = audio_file.metadata[required_field]
            if required_field_value is None or str(required_field_value).strip() == '':
                audio_files_with_missing_metadata.append(audio_file)
                break
    return audio_files_with_missing_metadata
