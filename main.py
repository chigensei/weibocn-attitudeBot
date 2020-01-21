# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 23:51:33 2020

Author: 智弦正@weibo (ycwei982)
This project is dedicated to reduce my anxiety.

"""

from bs4 import BeautifulSoup
import requests

"""
You need to config these to use the script.

1. The target link to the Weibo account. 

        Edit the variable "target_user_link".
        Open https://weibo.cn/ and access that user's page.
        Then copy the link. Paste it into the variable.

2. The cookies you are using when accessing https://weibo.cn.

        Please open "cookies.txt" file in the directory.
        Copy your cookie data strings in this order:
            "ALF", "SCF", "SSOLoginState", "SUB", "SUBP", "SUHB", "WEIBOCN_FROM", "_T_WM"
        Each data can only use one line.
        
"""
target_user_link = "https://weibo.cn/rmrb"


# Set requests' user-agent and cookies
# Initialize cookie names and dict
cookieNames = ["ALF", "SCF", "SSOLoginState", "SUB", "SUBP", "SUHB", "WEIBOCN_FROM", "_T_WM"]
realCookies = {}

# Get cookies from a text file
cookieFile = open("cookies.txt")
# cookieFileLines = cookieFile.readlines()

# Start adding cookies to dict realCookies
cookieAddCountTimes = 0
for eachline in cookieFile:
    realCookies[cookieNames[cookieAddCountTimes]] = eachline.strip('\n')
    cookieAddCountTimes += 1
# print(realCookies)

# Pretend as some regular browsers
requestHead = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

# Try getting each weibo attitude action link
def get_attitude_links(parsedPage, attitudeLinks):
    for link in parsedPage.find_all('a'):
        currentLink = link.get('href')
        if currentLink.find('https://weibo.cn/attitude/') >= 0:
            # print (currentLink)
            attitudeLinks.append(currentLink)
    # print(attitudeLinks)

# initialize weibo page and get links
def initialize_weibo_page(attitudeLinks):
    # weiboPage = open("./testpage.html", encoding='UTF-8')
    weiboPage = requests.get(target_user_link, cookies = realCookies, headers = requestHead)
    parser = BeautifulSoup(weiboPage.text, features="lxml")
    get_attitude_links(parser, attitudeLinks)

# Here we go!
def main():
    # First of all, we need to get links we are about to click
    attitudeLinks = []
    initialize_weibo_page(attitudeLinks)
    
main()
    
