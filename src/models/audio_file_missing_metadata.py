from src.models.audio_file import AudioFile


class AudioFileMissingMetadata:
    def __init__(self, audio_file: AudioFile):
        self.audio_file = audio_file
        self.missing_fields = []

    def add_missing_field(self, field: str):
        self.missing_fields.append(field)

    def missing_fields_as_string(self) -> str:
        return self.audio_file.file_name + " is missing: " + str(self.missing_fields)
