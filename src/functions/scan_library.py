from typing import List
import PIL

from src.models.genre import Genre

from ..models.artist import Artist
from ..models.audio_file import AudioFile
import utility
import os.path as osp
from .database import find_item_by_name, get_all_artists, init_database_object, save_item_to_database_if_does_not_exist, close_database


audio_file_extensions = utility.file_to_json_obj(
    osp.abspath("./ext/audio_codecs.json"))['extensions']
working_artist_set: set = []
existing_artists_from_db: set = []


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
    existing_artists_from_db = get_all_artists()
    for audio_file in audio_files:
        try:
            artists_from_file = audio_file_to_artists(audio_file, existing_artists_from_db)
            working_artist_set.append(artists_from_file)
        except ValueError as e:
            print(e)
        except PIL.UnidentifiedImageError as e:
            print(e)
    for artist in working_artist_set:
        print(artist)
        save_item_to_database_if_does_not_exist(artist)
    close_database()


def audio_file_to_artists(
    audio_file: AudioFile,
    existing_artists_from_db: set = [],
) -> List[Artist]:
    artist_list = []
    if audio_file != None and audio_file.metadata != None and audio_file.metadata['artist'] != None and audio_file.metadata['artist'].__str__() != '':
        artist_metadata_string = audio_file.metadata['artist'].__str__()
        artists_from_artist_tag = []
        for existing_artist in existing_artists_from_db:
            if existing_artist.name in artist_metadata_string:
                artist_list.append(existing_artist)
                artists_from_artist_tag = artist_metadata_string.split(existing_artist.name)
                artist_metadata_string = ''.join(artists_from_artist_tag)

        if ', ' in artist_metadata_string:
            artists_from_artist_tag = artist_metadata_string.split(', ')
        elif '& ' in artist_metadata_string:
            artists_from_artist_tag = artist_metadata_string.split('& ')
        elif '/ ' in artist_metadata_string:
            artists_from_artist_tag = artist_metadata_string.split('/ ')
        else:
            artists_from_artist_tag.append(artist_metadata_string)
        artists_from_artist_tag = list(filter(None, artists_from_artist_tag))

        for artist_name in artists_from_artist_tag:
            is_existing_artist = False
            for existing_artist in existing_artists_from_db:
                if existing_artist.is_same_artist_as(artist_name):
                    artist_list.append(existing_artist)
                    is_existing_artist = True
            if not is_existing_artist:
                genre_from_db = get_genre_from_audio_file(audio_file)
                artist = Artist(artist_name.strip(), [], [genre_from_db.id])
                artist_list.append(artist)
    return artist_list


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
