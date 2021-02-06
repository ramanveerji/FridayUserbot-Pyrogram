import logging
import os
import json
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

logger = logging.getLogger("IMAGE_DL")

base_url = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

class ImageDL:
    '''
    A Class For Image Downloader
    '''
    def __init__(self, driver):
        '''
        Pass Driver
        '''
        self.driver = driver
    def GoogleImageDL(self, keyword, limit, folder):
      '''
      Main Downloader Function
      Requires 3 parameter
      - Keyword
      - limit 
      - Folder (Path)
      '''
      driver = self.driver
      search_url = base_url + 'q=' + keyword
      driver.get(search_url)
      i=0
      while i<7:  
          driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
      try:
          driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
      except Exception as e:
          pass
      time.sleep(5)
      i+=1
      crawler = BeautifulSoup(driver.page_source,'html.parser')
      results = crawler.find_all(name = 'img',attrs = {'class':'t0fcAb'},limit=number)
      links = []
      for i in results:
          img_link = i['src']
          links.append(img_link)
      if len(links) == 0:
          logger.info("No Images Found !")
          return None
      for i, imagelink in enumerate(links):
          response = requests.get(imagelink)
          imagename = folder + '/' + keyword + str(i+1) + '.jpg'
          with open(imagename, 'wb') as file:
              file.write(response.content)
      driver.close()
      return folder

