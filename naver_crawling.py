import os
import sys
import urllib.request
import requests

cafes_data = []
page_count = 1

client_id = "YyUIKCNE8tklgwLFoYjE"
client_secret = "QFeMrw2MUb"
encText = urllib.parse.quote("윤석열")

for idx in range(page_count):
    url = "https://openapi.naver.com/v1/search/cafearticle?query=" + encText 
    #+ "&start=" + str(idx*10+1) # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과


    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode==200):
        result = requests.get(response.geturl(), headers={"X-Naver-Client-Id":client_id,"X-Naver-Client-Secret":client_secret})
        cafes_data.append(result.json())

    else:
        print("Error Code:" + rescode)

#naver-cafe only
naver_cafes_link = []

for page in cafes_data:
    page_cafes_link = []
    for item in page['items']:
        link = item['link']
        if "naver" in link:
            page_cafes_link.append(link)

    naver_cafes_link.append(page_cafes_link)

import numpy as np
import pandas as pd
from selenium import webdriver
from tqdm.notebook import tqdm
import pickle
import re
import ast

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import time

# 가상 크롬드라이버를 불러옴.
# 윈도우 10의 경우 chromedriver.exe
driver = webdriver.Chrome('driver/chromedriver')

naver_cafes_title = []

for n in tqdm(range(len(naver_cafes_link))):
    #print(n)
    cafes_page_title = []
    
    for idx in tqdm(range(len(naver_cafes_link[n]))):
        
        
# 긁어온 URL로 접속하기 
        try:
            driver.get(naver_cafes_link[n][idx])
            print(naver_cafes_link[n][idx])
            
        except:
            print("Timeout!")
            continue
        
        soup = BeautifulSoup(response, "html.parser")
        
# cafe 타이틀 긁어오기
        
        title = None
        
        try:
            item = soup.find('div', class_="article_info")
            title = item.find('h3', class_="tts_head").get_text()
            #print(title)

        except:
            title = "OUTLINK"
        
        #print(title)
        cafes_page_title.append(title)     
                
    naver_cafes_title.append(cafes_page_title)

    time.sleep(2)
    
    
print(naver_cafes_title[0])