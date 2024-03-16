from src.models.artist import Artist
from src.models.genre import Genre


non_existing_genre = Genre(name="I am not exist", akas=["i am not exist"])
non_existing_artist = Artist(name="I don't Exist", akas=["i don't exist"], genres=[non_existing_genre.id])
existing_genre = Genre(name="Dubstep", akas=["dubsteppa"])
existing_artist = Artist(name="Skrillex", akas=["Sonny Moore"], genres=[existing_genre.id])
duplicate_artist = Artist(name="Skrillex", akas=["Sonny Moore"], genres=[existing_genre.id])
similar_artist = Artist(name="Sonny Moore", akas=["Skrillex"], genres=[existing_genre.id])
artist_with_existing_akas = Artist(name="Unknown", akas=["Sonny Moore"], genres=[existing_genre.id])

# Audio File metadata mocks
solo_skrillex_audio_file = {'artist': 'Skrillex', 'title': 'First of the Year (Equinox)', 'genre': 'Dubstep'}