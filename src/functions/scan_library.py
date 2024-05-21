import PIL

from src.models.genre import Genre

from ..models.artist import Artist
from ..models.audio_file import AudioFile
import utility
import os.path as osp
from .database import find_item_by_name, init_database_object, save_item_to_database_if_does_not_exist, close_database


audio_file_extensions = utility.file_to_json_obj(
    osp.abspath("./ext/audio_codecs.json"))['extensions']
my_artists: set = []


def scan_library(directory: str):
    if utility.does_file_exist(directory):
        print("Scanning '{}'".format(directory))
        flattened_file_list = utility.flatten_folder(directory)
        audio_files = []
        for filepath in flattened_file_list:
            extension = osp.splitext(filepath)[1]
            if extension in audio_file_extensions:
                audio_file = AudioFile(filepath)
                audio_files.append(audio_file)
            else:
                print("'{}' is not a supported extension".format(extension))
    else:
        print('Given directory does not exist: ' + directory)
    init_database_object()
    for audio_file in audio_files:
        try:
            audio_file_to_artist(audio_file, my_artists)
        except ValueError as e:
            print(e)
        except PIL.UnidentifiedImageError as e:
            print(e)
    for artist in my_artists:
        print(artist)
        save_item_to_database_if_does_not_exist(artist)
    close_database()


def audio_file_to_artist(audio_file: AudioFile, existing_artists: set = []) -> Artist:
    artist = None
    if audio_file != None and audio_file.metadata != None and audio_file.metadata['artist'] != None and audio_file.metadata['artist'].__str__() != '':
        # Split using existing artist names first
        artist_metadata_string = audio_file.metadata['artist'].__str__()
        potential_artist_object = find_item_by_name(artist_metadata_string)
        artists_from_artist_tag = []
        if potential_artist_object is not None:
            artists_from_artist_tag = [potential_artist_object]
        elif ', ' in artist_metadata_string:
            artists_from_artist_tag = artist_metadata_string.split(', ')
        elif '& ' in artist_metadata_string:
            artists_from_artist_tag = artist_metadata_string.split('& ')
        elif '/ ' in artist_metadata_string:
            artists_from_artist_tag = artist_metadata_string.split('/ ')
        else:
            artists_from_artist_tag.append(artist_metadata_string)
        if type(artists_from_artist_tag[0]) is Artist:
            for artist_from_db in artists_from_artist_tag:
                existing_artists.append(artist_from_db)
                artist = artist_from_db
        else:
            for artist_name in artists_from_artist_tag:
                is_existing_artist = False
                for existing_artist in existing_artists:
                    if existing_artist.is_same_artist_as(artist_name):
                        is_existing_artist = True
                if not is_existing_artist:
                    genre_from_db = get_genre_from_audio_file(audio_file)
                    artist = Artist(artist_name.strip(), [], [genre_from_db.id])
                    existing_artists.append(artist)
    return artist


def get_genre_from_audio_file(audio_file: AudioFile):
    if audio_file != None and audio_file.metadata != None and audio_file.metadata['genre'] != None and audio_file.metadata['genre'].__str__() != '':
        genre_name = audio_file.metadata['genre'].__str__()
        potential_genre_object = find_item_by_name(genre_name)
        if potential_genre_object != None and type(potential_genre_object) == Genre:
            return potential_genre_object
        else:
            genre_to_add = Genre(genre_name, [])
            save_item_to_database_if_does_not_exist(genre_to_add)
            return genre_to_add
    return None
