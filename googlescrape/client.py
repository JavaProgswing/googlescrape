import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import requests
import re
from bs4 import BeautifulSoup
import validators
from .errors import *


def take_screenshot(browser, url, save_fn="capture.png"):
    if not url.startswith('http://') or not url.startswith('https://'):
        url = "https://" + url
    try:
        browser.get(url)
    except Exception as ex:
        if isinstance(ex, selenium.common.exceptions.WebDriverException):
            raise InvalidURLException("The url provided to take a screenshot was invalid!")

        elif isinstance(ex, selenium.common.exceptions.InvalidSessionIdException):
            g_chrome_options = webdriver.ChromeOptions()
            g_chrome_options.add_argument("window-size=1080x1080")
            g_chrome_options.add_argument("--headless")
            g_chrome_options.add_argument("--disable-dev-shm-usage")
            s = Service(ChromeDriverManager().install())
            browser = webdriver.Chrome(options=g_chrome_options, service=s)
            take_screenshot(url, save_fn)
            return
        else:
            raise ex
    try:
        browser.save_screenshot(save_fn)
    except:
        raise InvalidPathException("The file path provided to save the image might not be valid!")


def removetags(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)

    return cleantext


def validurl(url):
    isvalid = False

    try:
        isvalid = validators.url(url)
    except:
        pass
    return isvalid


def get_google_res(search):
    search = search.replace(" ", "+")
    url = f"https://www.google.com/search?q={search}"
    return requests.get(url, 'html.parser')


def site_search(url):
    html_doc = requests.get(url, 'html.parser').text
    soup = BeautifulSoup(html_doc, 'html.parser')

    result_string = ""
    para_str = ""

    result_string += removetags(str(soup.h1))
    list_para = soup.find_all('p')

    for para in list_para:
        para_str += f"{str(para)}\n"
    result_string += removetags(para_str)

    return result_string


class Client:
    def __init__(self):
        g_chrome_options = webdriver.ChromeOptions()
        g_chrome_options.add_argument("window-size=1080x1080")
        g_chrome_options.add_argument("--headless")
        g_chrome_options.add_argument("--disable-dev-shm-usage")
        s = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(options=g_chrome_options, service=s)
        self.browser = browser

    def image_search(self, search, savepath):
        search = search.replace(" ", "+")
        take_screenshot(self.browser, f"https://www.google.com/search?q={search}", savepath)

    def json_search(self, query):
        html_doc = get_google_res(query).text
        soup = BeautifulSoup(html_doc, 'html.parser')
        list_ = soup.find_all('h3')

        list_of_website_names = []
        list_of_website_urls = []

        for i in list_:
            list_of_website_names.append(i.string)
        list_ = soup.find_all('div')

        for i in list_:
            link = i.string

            if link is None:
                continue

            if not link.startswith('http:') or not link.startswith('https:'):
                link = "https://" + link

            link = link.replace(" ", "")
            link = link.replace("›", "/")

            if validurl(link):
                list_of_website_urls.append(link)

        json_result = {}

        for i in range(len(list_of_website_urls)):
            try:
                website_name = list_of_website_names[i]
                website_url = list_of_website_urls[i]
                json_result[website_name] = site_search(website_url)
            except:
                pass
        return json_result
