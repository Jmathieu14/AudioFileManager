from typing import List

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from webscraper.src.objects.track import Track

MAX_WAIT_SECONDS = 40
HTML_SONG_LIST: List[WebElement] = []
TRANSCRIBED_SONG_LIST: List[Track] = []
WEB_DRIVER = webdriver.Chrome(ChromeDriverManager().install())
WEB_DRIVER.implicitly_wait(10)
PLAYLIST_HOST = "https://soundcloud.com/spltpersonalty"
PLAYLIST_PATH = "/sets/kick-it-0ff"


def go_to_playlist_page():
    global HTML_SONG_LIST
    WEB_DRIVER.get(PLAYLIST_HOST + PLAYLIST_PATH)
    wait_until_page_loads()
    close_cookies_notice()
    HTML_SONG_LIST = get_song_list()
    get_all_songs_from_playlist()
    WEB_DRIVER.implicitly_wait(15)
    transcribe_song_list()


def transcribe_song_list():
    global TRANSCRIBED_SONG_LIST
    for i in range(0, HTML_SONG_LIST.__len__()):
        html = HTML_SONG_LIST.__getitem__(i)
        uploaded_by = html.find_element_by_css_selector(".trackItem__username").text
        url = html.find_element_by_css_selector(".trackItem__trackTitle").get_attribute("href")
        title = html.find_element_by_css_selector(".trackItem__trackTitle").text
        track = Track(title, url, uploaded_by)
        TRANSCRIBED_SONG_LIST.append(track)
        track.print()


def get_all_songs_from_playlist():
    global HTML_SONG_LIST
    scroll_down_until_all_songs_loaded()
    WEB_DRIVER.implicitly_wait(20)
    HTML_SONG_LIST = get_song_list()


def print_html_song_list():
    for i in range(0, HTML_SONG_LIST.__len__()):
        print(HTML_SONG_LIST.__getitem__(i))


def wait_until_page_loads():
    WebDriverWait(WEB_DRIVER, MAX_WAIT_SECONDS).until(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, "#app a.announcement__dismiss[title='Dismiss']")))


def close_cookies_notice():
    cookie_dismiss_button = WEB_DRIVER.find_element_by_css_selector("#app a.announcement__dismiss[title='Dismiss']")
    cookie_dismiss_button.click()


def get_song_list() -> List[WebElement]:
    return WEB_DRIVER.find_elements_by_css_selector(".trackItem")


def scroll_down_until_all_songs_loaded():
    try:
        loading_element = WEB_DRIVER.find_element_by_css_selector("ul + .loading")
        if loading_element is not None:
            scroll_down()
            WEB_DRIVER.implicitly_wait(5)
            scroll_down_until_all_songs_loaded()
    except NoSuchElementException:
        pass


def scroll_down():
    html = WEB_DRIVER.find_element_by_css_selector("body")
    html.send_keys(Keys.END)
