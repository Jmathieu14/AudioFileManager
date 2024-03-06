import uuid
from src.models.aka import Aka
from src.aka_util import akas_are_equal, akas_to_dict, handle_akas_list

from utility import are_strings_equal_ignore_case


class Artist:
    def __init__(self, name: str, akas: list[Aka], genres: list, id=None) -> None:
        self.name = name
        self.akas = handle_akas_list(akas)
        self.genres = genres
        self.id = id if id is not None else uuid.uuid4().__str__()

    def is_same_artist_as(self, other_name: str) -> bool:
        if are_strings_equal_ignore_case(self.name, other_name):
            return True
        for i in range(0, self.akas.__len__()):
            if are_strings_equal_ignore_case(self.akas[i], other_name):
                return True
        return False

    def add_aka_name(self, new_name: str) -> None:
        new_aka = Aka(new_name)
        self.akas.append(new_aka)

    def add_genre(self, genre_id: str) -> None:
        self.genres.append(genre_id)

    def to_dict(self) -> dict[str, list]:
        return {
            "type": "artist",
            "name": self.name,
            "akas": akas_to_dict(self.akas),
            "genres": self.genres,
            "id": self.id
        }

    def __eq__(self, __value: object) -> bool:
        if type(__value) == type(self):
            return self.name == __value.name and akas_are_equal(self.akas, __value.akas) and self.genres == __value.genres and self.id == __value.id
        else:
            return False

    def __str__(self) -> str:
        return "Artist: {}, aka: {}, genres: {}, id: {}".format(self.name, self.akas, self.genres, self.id)
