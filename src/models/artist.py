import uuid

from utility import are_strings_equal_ignore_case


class Artist:
    def __init__(self, name: str, aka: list, genres: list, id=None) -> None:
        self.name = name
        self.aka = aka
        self.genres = genres
        self.id = id if id is not None else uuid.uuid4()

    def is_same_artist_as(self, other_name: str) -> bool:
        if are_strings_equal_ignore_case(self.name, other_name):
            return True
        for i in range (0, self.aka.__len__()):
            if are_strings_equal_ignore_case(self.aka[i], other_name):
                return True
        return False
    
    def add_aka_name(self, new_name: str) -> None:
        self.aka.append(new_name)

    def add_genre(self, genre_id: str) -> None:
        self.genres.append(genre_id)

    def __str__(self) -> str:
        return "Artist: {}, aka: {}, genres: {}, id: {}".format(self.name, self.aka, self.genres, self.id)
