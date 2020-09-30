#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 00:44:00 2020

@author: deviantpadam
"""

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import sqlite3
from datetime import datetime

# urls1 = ['https://www.boomlive.in/fake-news','https://www.indiatoday.in/fact-check','https://www.altnews.in/topics/news/']
# urls2 = ['https://thelogicalindian.com/fact-check']
# urls3 = ['https://www.opindia.com/category/fact-check/']
# urls4 = ['https://www.livehindustan.com/tags/hindustan-fact-check']

# def getData1(Url):
#     URL = Url
#     links = []
#     titles = []
#     agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
#     page = requests.get(URL,headers=agent)
#     soup = BeautifulSoup(page.content,'html.parser')
#     job_elems = soup.find_all('h2')
#     for i in job_elems:
#         try:
#             link = i.find('a')['href']
#             title = i.find('a').contents[0]
#         except:
#             break
#         links.append(link)
#         titles.append(title)
#     return links,titles

# def getData2(Url):
#     URL = Url
#     links = []
#     titles = []
#     agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
#     page = requests.get(URL,headers=agent)
#     soup = BeautifulSoup(page.content,'html.parser')
#     job_elems = soup.find_all('h4')
#     for i in job_elems:
#         try:
#             link = i.find('a')['href']
#             title = i.find('a').contents[0]
#         except:
#             break
#         links.append(link)
#         titles.append(title)
#     return links,titles


# def getData3(Url):
#     URL = Url
#     links = []
#     titles = []
#     page = requests.get(URL)
#     soup = BeautifulSoup(page.content,'html.parser')
#     job_elems = soup.find_all('h3',class_='entry-title td-module-title')
#     for i in job_elems:
#         try:
#             link = i.find('a')['href']
#             title = i.find('a').contents[0]
#         except:
#             break
#         links.append(link)
#         titles.append(title)
#     return links, titles

# def getData4(Url):
#     URL = Url
#     links = []
#     titles = []
#     agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
#     page = requests.get(URL,headers=agent)
#     soup = BeautifulSoup(page.content,'html.parser')
#     job_elems = soup.find_all('h4',class_="hindustan-link")
#     for i in job_elems:
#         try:
#             link = i.find('a')['href']
#             title = i.find('a').contents[0]
#         except:
#             break
#         links.append(link)
#         titles.append(title)
#     return links, titles

def fetch1():
    URL = 'https://www.boomlive.in/fake-news'
    links = []
    titles = []
    img = []
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    page = requests.get(URL,headers=agent)
    soup = BeautifulSoup(page.content,'html.parser')
    job_elems = soup.find_all('figure')
    for i in job_elems:
        img.append(i.img['data-src'])
        titles.append(i.img['title'])
        links.append(i.a['href'])
        
    links = [(re.findall(r'(https?://\S+/)', URL))[0][:-1]+ f for f in links]
    
    return links,titles,img

# fetch1()

def fetch2():
    links = []
    titles = []
    img = []
    URL = 'https://www.altnews.in/topics/news/'
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    page = requests.get(URL,headers=agent)
    soup = BeautifulSoup(page.content,'html.parser')
    job_elems = soup.find_all('div',class_='herald-post-thumbnail herald-format-icon-middle')
    for i in job_elems:
        img.append(i.img['src'])
        titles.append(i.a['title'])
        links.append(i.a['href'])
    
    return links,titles,img

# fetch2()

def fetch3():
    links = []
    titles = []
    img = []
    URL = 'https://www.indiatoday.in/fact-check'
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    page = requests.get(URL,headers=agent)
    soup = BeautifulSoup(page.content,'html.parser')
    job_elems = soup.find_all('div',class_='pic')
    job_elems2 = soup.find_all('div',class_='detail')
    for i in job_elems:
        img.append(i.img['src'])
    for i in job_elems2:
        titles.append(i.h2['title'])
        links.append(i.a['href'])     
        
    links = [(re.findall(r'(https?://\S+/)', URL))[0][:-1]+ f for f in links]
    
    return links,titles,img

# fetch3()

def fetch4():
    links = []
    titles = []
    img = []
    URL = 'https://thelogicalindian.com/fact-check'
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    page = requests.get(URL,headers=agent)
    soup = BeautifulSoup(page.content,'html.parser')
    job_elems = soup.find_all('div',class_='article_template2')
    for i in job_elems:
        img.append(i.img['data-src'])
        titles.append(i.img['title'])
        links.append(i.a['href'])

    links = [(re.findall(r'(https?://\S+/)', URL))[0][:-1]+ f for f in links]
    
    return links,titles,img

# fetch4()


def fetch5():
    links = []
    titles = []
    img = []
    URL = 'https://www.livehindustan.com/tags/hindustan-fact-check'
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    page = requests.get(URL,headers=agent)
    soup = BeautifulSoup(page.content,'html.parser')
    soup = BeautifulSoup(page.content,'html.parser')
    job_elems = soup.find_all('div',class_='upper-first')
    for i in job_elems:
        img.append(i.img['data-src'])
        titles.append(i.img['title'])
        links.append(i.a['href'])
        
    links = [(re.findall(r'(https?://\S+/)', URL))[0][:-1]+ f for f in links]
    
    return links,titles,img

# fetch5()


def fetch6():
    links = []
    titles = []
    img = []
    URL = 'https://www.opindia.com/category/fact-check/'
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    page = requests.get(URL,headers=agent)
    soup = BeautifulSoup(page.content,'html.parser')
    job_elems = soup.find_all('div',class_='td-module-container td-category-pos-image')

    for i in job_elems:
        titles.append(i.div.div.a['title'])
        links.append(i.div.div.a['href'])
        img.append(re.findall(r'(https?://\S+)',i.div.div.a.span['style'])[0])
    
        
    return links, titles, img

# fetch6()
    
def caller():
    links = []
    titles = []
    img_links = []
    
    link, title, img = fetch1()
    links+=link
    titles+=title
    img_links+=img
    
    link, title, img = fetch2()
    links+=link
    titles+=title
    img_links+=img
    
    link, title, img = fetch3()
    links+=link
    titles+=title
    img_links+=img
    
    link, title, img = fetch4()
    links+=link
    titles+=title
    img_links+=img
    
    link, title, img = fetch5()
    links+=link
    titles+=title
    img_links+=img
    
    link, title, img = fetch6()
    links+=link
    titles+=title
    img_links+=img
    
    return links,titles,img_links

link,title,img = caller()
datetime.today().strftime('%d-%m-%y')
pd.to_datetime('today').date()
df = pd.DataFrame({'links':link,'titles':title,'img_link':img})
df['date'] = pd.to_datetime('today').date()
df.drop_duplicates(subset=['links','titles'],inplace=True)

conn = sqlite3.connect('db2.sqlite')

conn.execute('''CREATE TABLE IF NOT EXISTS fake_news(
    date text,
    links text,
    titles text,
    img_link text,
    unique (links,titles,img_link)
    );''')

# curr = conn.cursor()

df.to_sql('fake_news',conn,index=False,if_exists='append')

# cur = conn.cursor()
# cur.execute('SELECT * FROM fake_news')
# results = cur.fetchall()

# results[0]
