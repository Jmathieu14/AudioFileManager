from typing import List
from utility import create_file_if_dne, create_folder_if_dne, does_file_exist
import os.path as osp

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import InvalidSessionIdException

from webscraper.src.objects.track import Track

MAX_WAIT_SECONDS = 40
HTML_SONG_LIST: List[WebElement] = []
PLAYLIST_URL_LIST: List[str] = []
TRANSCRIBED_SONG_LIST: List[Track] = []
WEB_DRIVER = webdriver.Chrome()
WEB_DRIVER.implicitly_wait(10)
PLAYLIST_HOST = "https://soundcloud.com/spltpersonalty"
PLAYLIST_PATH = "sets/gargantuan-dirty-dubstep-beats"
FILE_DIR = "webscraper"
SETS_DIR_PATH = osp.abspath("{0}\\{1}\\sets".format(osp.curdir, FILE_DIR))
temp_playlist_filter_list = []
# temp_playlist_filter_list = ["https://soundcloud.com/spltpersonalty/sets/somg-uh-duh-week-vol-4", "https://soundcloud.com/spltpersonalty/sets/song-de-la-week-vol-3", "https://soundcloud.com/spltpersonalty/sets/2022-blues-clues-n-bops"]

def handle_file_exists_error():
    WEB_DRIVER.close()
    return FileExistsError


def transcribed_song_list_to_string():
    song_list_as_text = ""
    for song in TRANSCRIBED_SONG_LIST:
        song_list_as_text = song_list_as_text + song.__str__() + "\n"
    return song_list_as_text


def save_transcribed_song_list_to_csv(url: str):
    fileName = url.__str__().replace(PLAYLIST_HOST, "")
    filePath = osp.abspath("{0}\\{1}\\{2}.csv".format(osp.curdir, FILE_DIR, fileName))
    if not does_file_exist(filePath):
        create_folder_if_dne(SETS_DIR_PATH)
        print("Writing to: {0}".format(filePath))
        content_to_write = transcribed_song_list_to_string()
        create_file_if_dne(filePath, content_to_write)
    else:
        return handle_file_exists_error()


def save_all_playlists_to_file():
    global HTML_SONG_LIST
    global PLAYLIST_URL_LIST
    get_all_playlists_from_sets_page()
    for i in range (0, PLAYLIST_URL_LIST.__len__()):
        HTML_SONG_LIST = []
        url = PLAYLIST_URL_LIST.__getitem__(i)
        if url in temp_playlist_filter_list:
            save_playlist_info_from(url)
        elif temp_playlist_filter_list is None or temp_playlist_filter_list.__len__() == 0:
            save_playlist_info_from(url)
    WEB_DRIVER.implicitly_wait(20)
    WEB_DRIVER.close()


def save_playlist_info_from(url: str):
    global HTML_SONG_LIST
    try:
        WEB_DRIVER.get(url)
        WEB_DRIVER.implicitly_wait(10)
        HTML_SONG_LIST = get_song_list()
        get_all_songs_from_playlist()
        WEB_DRIVER.implicitly_wait(15)
        transcribe_song_list()
        save_transcribed_song_list_to_csv(url)
    except InvalidSessionIdException as e:
        print("InvalidSession for '{}'".format(url))



def go_to_playlist_page():
    global HTML_SONG_LIST
    WEB_DRIVER.get(PLAYLIST_HOST + PLAYLIST_PATH)
    wait_until_playlist_page_loads()
    close_cookies_notice()
    HTML_SONG_LIST = get_song_list()
    get_all_songs_from_playlist()
    WEB_DRIVER.implicitly_wait(15)
    transcribe_song_list()


def transcribe_song_list():
    global TRANSCRIBED_SONG_LIST
    for i in range(0, HTML_SONG_LIST.__len__()):
        html = HTML_SONG_LIST.__getitem__(i)
        uploaded_by = html.find_element(By.CSS_SELECTOR, ".trackItem__username").text
        url = html.find_element(By.CSS_SELECTOR, ".trackItem__trackTitle").get_attribute("href")
        title = html.find_element(By.CSS_SELECTOR, ".trackItem__trackTitle").text
        track = Track(title, url, uploaded_by)
        TRANSCRIBED_SONG_LIST.append(track)


def save_playlist_paths_to_global_list(playlist_url_items):
    global PLAYLIST_URL_LIST
    for i in range(0, playlist_url_items.__len__()):
        element = playlist_url_items.__getitem__(i)
        url = element.get_attribute("href")
        PLAYLIST_URL_LIST.append(url)


def get_all_playlists_from_sets_page():
    WEB_DRIVER.get(PLAYLIST_HOST + "/sets")
    WEB_DRIVER.implicitly_wait(15)
    scroll_down_until_all_playlists_loaded()
    playlist_url_items = get_playlists()
    save_playlist_paths_to_global_list(playlist_url_items)


def get_all_songs_from_playlist():
    global HTML_SONG_LIST
    scroll_down_until_all_songs_loaded()
    WEB_DRIVER.implicitly_wait(20)
    HTML_SONG_LIST = get_song_list()


def print_html_song_list():
    for i in range(0, HTML_SONG_LIST.__len__()):
        print(HTML_SONG_LIST.__getitem__(i))


def wait_until_playlist_page_loads():
    WebDriverWait(WEB_DRIVER, MAX_WAIT_SECONDS).until(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, "#app a.announcement__dismiss[title='Dismiss']")))


def wait_until_playlists_page_loads():
    WebDriverWait(WEB_DRIVER, MAX_WAIT_SECONDS).until(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, "#content .soundList .soundList__item:first-child .soundTitle__playButton")))


def close_cookies_notice():
    cookie_dismiss_button = WEB_DRIVER.find_element(By.CSS_SELECTOR, "#app a.announcement__dismiss[title='Dismiss']")
    cookie_dismiss_button.click()


def get_song_list() -> List[WebElement]:
    return WEB_DRIVER.find_elements(By.CSS_SELECTOR, ".trackItem")


def get_playlists() -> List[WebElement]:
    return WEB_DRIVER.find_elements(By.CSS_SELECTOR, ".soundTitle__title")


def scroll_down_until_all_songs_loaded():
    try:
        loading_element = WEB_DRIVER.find_element(By.CSS_SELECTOR, "ul + .loading")
        if loading_element is not None:
            scroll_down()
            WEB_DRIVER.implicitly_wait(5)
            scroll_down_until_all_songs_loaded()
    except NoSuchElementException:
        pass


def scroll_down_until_all_playlists_loaded():
    try:
        loading_element = WEB_DRIVER.find_element(By.CSS_SELECTOR, "ul + .loading")
        if loading_element is not None:
            scroll_down()
            WEB_DRIVER.implicitly_wait(5)
            scroll_down_until_all_playlists_loaded()
    except NoSuchElementException:
        pass


def scroll_down():
    html = WEB_DRIVER.find_element(By.CSS_SELECTOR, "body")
    html.send_keys(Keys.END)
