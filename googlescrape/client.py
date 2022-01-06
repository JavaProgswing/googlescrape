import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import requests
import re
from bs4 import BeautifulSoup
import validators
from .errors import *
def take_screenshot(browser,url, save_fn="capture.png"):
    if not url.startswith('http://') and not url.startswith('https://'):
        url="https://"+url
    try:
        browser.get(url)
    except Exception as ex:
        if isinstance(ex,selenium.common.exceptions.WebDriverException):
            raise InvalidURLException("The url provided to take a screenshot was invalid!")
            return
        elif isinstance(ex,selenium.common.exceptions.InvalidSessionIdException):
            gChromeOptions = webdriver.ChromeOptions()
            gChromeOptions.add_argument("window-size=1080x1080")
            gChromeOptions.add_argument("--disable-dev-shm-usage")
            s=Service(ChromeDriverManager().install())
            browser = webdriver.Chrome(options=gChromeOptions,service=s)
            take_screenshot(url,save_fn)
            return
        else:
            raise ex
            return
    try:
        browser.save_screenshot(save_fn)
    except:
        raise InvalidPathException("The file path provided to save the image might not be valid!")
        return
def removetags(raw_html):
  CLEANR = re.compile('<.*?>') 
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext
def validurl(theurl):
    isvalid = False
    try:
        isvalid = validators.url(theurl)
    except:
        pass
    return isvalid
def getgooglecode(search):
    search=search.replace(" ","+")
    url=f"https://www.google.com/search?q={search}"
    return requests.get(url, 'html.parser')
def sitesearch(url):
    html_doc=requests.get(url, 'html.parser').text
    soup = BeautifulSoup(html_doc, 'html.parser')
    resultstring=""
    resultstring=resultstring+removetags(str(soup.h1))
    listpara=soup.find_all('p')
    parastr=""
    for para in listpara:
        parastr=parastr+str(para)+"\n"
    resultstring=resultstring+removetags(parastr)
    return resultstring
class Client:
    def __init__(self):
        gChromeOptions = webdriver.ChromeOptions()
        gChromeOptions.add_argument("window-size=1080x1080")
        gChromeOptions.add_argument("--disable-dev-shm-usage")
        s=Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(options=gChromeOptions,service=s)
        self.browser=browser
    def imagesearch(self,search,savepath):
        search=search.replace(" ","+")
        take_screenshot(self.browser,f"https://www.google.com/search?q={search}",savepath)
    def googlescrape(query):
        html_doc=(getgooglecode(query).text)
        soup = BeautifulSoup(html_doc, 'html.parser')
        list=soup.find_all('h3')
        listofwebsitenames=[]
        for i in list:
            listofwebsitenames.append(i.string)
        list=soup.find_all('div')
        listofwebsiteurls=[]
        for i in list:
            link=i.string
            if link is None:
                continue
            if not link.startswith('http:') or not link.startswith('https:'):
                link="https://"+link
            link=link.replace(" ","")
            link=link.replace("›","/")
            if validurl(link):
                listofwebsiteurls.append(link)
        jsonresult={}
        for i in len(listofwebsiteurls):
            try:
                websitename=listofwebsitenames[i]
                websiteurl=listofwebsiteurls[i]
                jsonresult[websitename]=sitesearch(websiteurl)
            except:
                pass
        return jsonresult



