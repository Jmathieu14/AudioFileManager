from src.models.artist import Artist
from src.models.genre import Genre


non_existing_genre = Genre(name="I am not exist", aka=["i am not exist"])
non_existing_artist = Artist(name="I don't Exist", aka=["i don't exist"], genres=[non_existing_genre.id])
existing_genre = Genre(name="Dubstep", aka=["dubsteppa"])
existing_artist = Artist(name="Skrillex", aka=["Sonny Moore"], genres=[existing_genre.id])
