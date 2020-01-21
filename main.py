# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 23:51:33 2020

Author: 智弦正@weibo (ycwei982)
This project is dedicated to reduce my anxiety.

"""

from bs4 import BeautifulSoup
import time
import requests

"""
TODO:
    1. Get rid of duplicate likes. Weibo sometimes cleans user side Like button as clickable even you already liked that post
    2. User-friendly outputs e.g. "LIKE ACTION SUCCESS, FAILED, try-catch"
    3. Server based plan
"""

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

# access links we get from initializing
def attitude_access(accessURL):
    # Since WAP weibo made Like button to a link, we only need to "get" that action URL
    requests.get(accessURL, cookies = realCookies, headers = requestHead)


# Here we go!
"""
假如你是李华，你有一个在微博上互粉的好友叫 Lily，你很关心她，她也很关心你，但不知道为什么，她不给你的微博点赞。
虽然你知道她一直都很忙，但你的心很涼、很失落，于是决定写封信给她，来表达自己的焦虑。

作文要求：
1. 表达誠恳的态度，要让她知道你是真的很关心她
2. 提出合理的解决方案。
3. 不少于 100 行代码。
"""
def main():
    # Dear Lily, I know you don't have enough time to read my posts on Weibo. So I'm writing to you on GitHub in order to provide a solutions for you.
    # First and foremost, we need to get links we are about to click. I choose to store them in an array
    attitudeLinks = []
    initialize_weibo_page(attitudeLinks)
    
    # What's next, I think it's a time for you to click those links. I know you don't have very spare time for visiting my Weibo account.
    # So here is my gift, it's an automation code piece, which will help you make my heart happy.
    for eachlink in attitudeLinks:
        attitude_access(eachlink)
        # In addition, Weibo doesn't let us access so fast, we need to give its servers a break.
        time.sleep(2) # In my opinion, 2 seconds is enough for a computer to sleep.
    
main()

"""
I'd like to appreciate it if you could give me reply at your earliest convenience.

Sincerely,
Li Hua
"""    
