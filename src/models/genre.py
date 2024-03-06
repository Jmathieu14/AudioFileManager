import uuid
from src.models.aka import Aka
from src.aka_util import akas_are_equal, akas_to_dict, handle_akas_list

from utility import are_strings_equal_ignore_case


class Genre:
    def __init__(self, name: str, akas: list[Aka], id=None) -> None:
        self.name = name
        self.akas = handle_akas_list(akas)
        self.id = id if id is not None else uuid.uuid4().__str__()

    def is_same_genre_as(self, other_name: str) -> bool:
        if are_strings_equal_ignore_case(self.name, other_name):
            return True
        for i in range (0, self.akas.__len__()):
            if are_strings_equal_ignore_case(self.akas[i], other_name):
                return True
        return False

    def to_dict(self) -> dict[str, list]:
        return {
            "type": "genre",
            "name": self.name,
            "akas": akas_to_dict(self.akas),
            "id": self.id
        }
    
    def __eq__(self, __value: object) -> bool:
        if type(__value) == type(self):
            return self.name == __value.name and akas_are_equal(self.akas, __value.akas) and self.id == __value.id
        else:
            return False
    
    def add_aka_name(self, new_name: str) -> None:
        new_aka = Aka(new_name)
        self.akas.append(new_aka)
