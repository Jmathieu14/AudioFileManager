from typing import List
import PIL

from src.functions.audio_file_util import get_audio_files_from_directory
from src.models.genre import Genre

from ..models.artist import Artist
from ..models.audio_file import AudioFile
import utility
import os.path as osp
from .database import (
    find_item_by_name,
    get_all_artists,
    init_database_object,
    save_item_to_database_if_does_not_exist,
    close_database,
)


working_new_artists_set: set = set()
existing_artists_from_db: List = []


def scan_library(directory: str):
    audio_files = get_audio_files_from_directory(directory)
    init_database_object()
    existing_artists_from_db = get_all_artists()
    for audio_file in audio_files:
        try:
            audio_file_to_artists(audio_file, working_new_artists_set, existing_artists_from_db)
        except ValueError as e:
            print(e)
        except PIL.UnidentifiedImageError as e:
            print(e)
    for artist in working_new_artists_set:
        print(artist)
        save_item_to_database_if_does_not_exist(artist)
    close_database()


def audio_file_to_artists(
    audio_file: AudioFile,
    working_new_artists_set: set = set(),
    existing_artists_from_db: List = [],
) -> List[Artist]:
    """Parses artist metadata from the given audio file to provide a list of pertaining Artist objects

    Args:
        audio_file (AudioFile): The audio file to be analyzed
        working_new_artists_set (set, optional): an in memory collection of artists found while parsing multiple audio files to be saved to the database later. Defaults to set().
        existing_artists_from_db (List, optional): a list of Artist objects that represent the existing artists in the database. Defaults to [].

    Returns:
        List[Artist]: A list of Artist objects that pertain to the given AudioFile
    """
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
            is_in_working_new_artists_set = False
            for working_new_artist in working_new_artists_set:
                if working_new_artist.is_same_artist_as(artist_name):
                    artist_list.append(working_new_artist)
                    is_in_working_new_artists_set = True
            if not is_in_working_new_artists_set:
                genre_from_db = get_genre_from_audio_file(audio_file)
                artist = Artist(artist_name.strip(), [], [genre_from_db.id])
                working_new_artists_set.add(artist)
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
