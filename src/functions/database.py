from tinydb import Query, TinyDB
from src.models.artist import Artist
from config import get_database_file_path
from src.models.genre import Genre
import re


database_initialized = False
local_database: any


def get_database() -> TinyDB | None:
    if not database_initialized:
        init_database_object()
    return local_database


def init_database_object() -> None:
    global local_database, database_initialized
    my_database_file_path = get_database_file_path()
    local_database = TinyDB(my_database_file_path)
    database_initialized = True


def close_database() -> None:
    if database_initialized and local_database != None:
        local_database.close()


def get_item_by_uuid(id: str) -> Artist | Genre:
    q = Query()
    items = local_database.search(q.id == id)
    return _items_to_artist_or_genre(items)


def find_item_by_name(name: str, ignore_case=True) -> Artist | Genre | None:
    q = Query()
    aka = Query()
    items = None
    if not ignore_case:
        items = _handle_find_item_by_name_respect_case(name)
    else:
        items = local_database.search(q.name.matches(name, re.IGNORECASE))
        if items.__len__() == 0:
            items = local_database.search(q.akas.any(aka.name.matches(name, re.IGNORECASE)))
    return _items_to_artist_or_genre(items)


def _handle_find_item_by_name_respect_case(name: str) -> Artist | Genre | None:
    q = Query()
    aka = Query()
    items = local_database.search(q.name.matches(name))
    if items.__len__() == 0:
        items = local_database.search(q.akas.any(aka.name.matches(name)))
    return items


def _items_to_artist_or_genre(items: list) -> Artist | Genre | None:
    item = None
    if items != None and items.__len__() == 1:
        item = items[0]
        if item['type'] == 'artist':
            item = Artist(item['name'], item['akas'], item['genres'], item['id'])
        elif item['type'] == 'genre':
            item = Genre(item['name'], item['akas'], item['id'])
    return item


def does_item_exist(item: Artist | Genre) -> bool:
    if find_item_by_name(item.name) is None:
        for aka in item.akas:
            if find_item_by_name(aka.name) != None:
                return True
        return False
    else:
        return True


def save_item_to_database_if_does_not_exist(item: Artist | Genre):
    if not does_item_exist(item):
        local_database.insert(item.to_dict())