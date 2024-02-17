from tinydb import Query, TinyDB
from src.models.artist import Artist
from config import get_database_file_path
from src.models.genre import Genre


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
    item = None
    if items.__len__() == 1:
        item = items[0]
        if item['type'] == 'artist':
            item = Artist(item['name'], item['aka'], item['genres'], item['id'])
        elif item['type'] == 'genre':
            item = Genre(item['name'], item['aka'], item['id'])
    return item


def does_item_exist(item: Artist | Genre) -> bool:
    name = item.name
    Item = Query()
    return True if local_database.search(Item.name == name) else False


def save_item_to_database_if_does_not_exist(item: Artist | Genre):
    pass