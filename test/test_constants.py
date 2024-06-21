from src.models.artist import Artist
from src.models.genre import Genre


non_existing_genre = Genre(name="I am not exist", akas=["i am not exist"])
non_existing_artist = Artist(name="I don't Exist", akas=["i don't exist"], genres=[non_existing_genre.id])
existing_genre = Genre(name="Dubstep", akas=["dubsteppa"])
drum_and_bass = Genre(name="Drum & Bass", akas=["Drum and Bass"])
existing_artist = Artist(name="Skrillex", akas=["Sonny Moore"], genres=[existing_genre.id])
duplicate_artist = Artist(name="Skrillex", akas=["Sonny Moore"], genres=[existing_genre.id])
similar_artist = Artist(name="Sonny Moore", akas=["Skrillex"], genres=[existing_genre.id])
artist_with_existing_akas = Artist(name="Unknown", akas=["Sonny Moore"], genres=[existing_genre.id])
artist_with_ampersand = Artist(name="Camo & Krooked", akas=[], genres=[drum_and_bass.id])

# Audio File metadata mocks
solo_skrillex_audio_file = {'artist': 'Skrillex', 'title': 'First of the Year (Equinox)', 'genre': 'Dubstep'}
solo_skrillex_audio_file_with_aka_genre = {'artist': 'Skrillex', 'title': 'First of the Year (Equinox)', 'genre': 'dubsteppa'}
solo_camo_and_krooked_audio_file = {'artist': 'Camo & Krooked', 'title': 'Mindset', 'genre':'Drum & Bass'}
dual_artist_camo_and_krooked_and_tasha_baxter_audio_file = {'artist': 'Camo & Krooked, Tasha Baxter', 'title': 'Ooooh La LA', 'genre':'Drum & Bass'}