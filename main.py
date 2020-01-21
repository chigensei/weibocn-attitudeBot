# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 23:51:33 2020

This project is dedicated to reduce my anxiety.

"""

from bs4 import BeautifulSoup
import requests

# initialize weibo page
weiboPage = open("./testpage.html", encoding='UTF-8')
parsedPage = BeautifulSoup(weiboPage, features="lxml")

# Try printing out each weibo like link
for link in parsedPage.find_all('a'):
    currentLink = link.get('href')
    if currentLink.find('https://weibo.cn/attitude/') >= 0:
        print (currentLink)
        
