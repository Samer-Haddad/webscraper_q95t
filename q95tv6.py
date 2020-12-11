#!/usr/bin/env python3.8
# This webscraper retrieves price for samsung-75-inch-q95t Version:6

import requests
import urllib
import random
import time
import pathlib
import tkinter as tk
import webbrowser
from math import inf
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver


user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)',
    'DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)',
    'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
    'Sogou Pic Spider/3.0( http://www.sogou.com/docs/help/webmasters.htm#07)',
    'Sogou head spider/3.0( http://www.sogou.com/docs/help/webmasters.htm#07)',
    'Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)',
    'Sogou Orion spider/3.0( http://www.sogou.com/docs/help/webmasters.htm#07)',
    'Sogou-Test-Spider/4.0 (compatible; MSIE 5.5; Windows 98)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Exabot-Thumbnails)',
    'Mozilla/5.0 (compatible; Exabot/3.0; +http://www.exabot.com/go/robot)',
    'facebot',
    'facebookexternalhit/1.0 (+http://www.facebook.com/externalhit_uatext.php)',
    'facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)',
    'ia_archiver (+http://www.alexa.com/site/help/webmasters; crawler@alexa.com)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]


ao = 'https://www.appliancesonline.com.au/product/samsung-75-inch-q95t-4k-uhd-hdr-smart-qled-tv-qa75q95tawxxy'
jbhifi = 'https://www.jbhifi.com.au/products/samsung-q95t-75-qled-ultra-hd-4k-smart-tv-2020'
ac = 'https://www.appliancecentral.com.au/qa75q95tawxxy-samsung-75-inch-q95t-qled-smart-4k-tv-2020-tv?language=en&currency=AUD'
videopro = 'https://www.videopro.com.au/p-13538-samsung-75-qa75q95taw-ultra-hd-qled-smart-tv.aspx'
binglee = 'https://www.binglee.com.au/samsung-qa75q95tawxxy-75-inch-q95t-qled-smart-4k-tv'
harveynorman = 'https://www.harveynorman.com.au/samsung-75-inch-q95t-4k-qled-smart-tv.html'
thegoodguys = 'https://www.thegoodguys.com.au/samsung-75-inches-q95t-4k-uhd-smart-qled-tv-qa75q95tawxxy'

urls = {'Appliances Online':'https://www.appliancesonline.com.au/product/samsung-75-inch-q95t-4k-uhd-hdr-smart-qled-tv-qa75q95tawxxy', 
        'JB-HiFi':'https://www.jbhifi.com.au/products/samsung-q95t-75-qled-ultra-hd-4k-smart-tv-2020', 
        'Appliance Central':'https://www.appliancecentral.com.au/qa75q95tawxxy-samsung-75-inch-q95t-qled-smart-4k-tv-2020-tv?language=en&currency=AUD', 
        'Videopro':'https://www.videopro.com.au/p-13538-samsung-75-qa75q95taw-ultra-hd-qled-smart-tv.aspx', 
        'Bing Lee':'https://www.binglee.com.au/samsung-qa75q95tawxxy-75-inch-q95t-qled-smart-4k-tv', 
        'Harvey Norman':'https://www.harveynorman.com.au/samsung-75-inch-q95t-4k-qled-smart-tv.html', 
        'The Good Guys':'https://www.thegoodguys.com.au/samsung-75-inches-q95t-4k-uhd-smart-qled-tv-qa75q95tawxxy'}

chromedriver_path = str(pathlib.Path(__file__).parent.absolute())
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--log-level=3')
options.add_argument('--silent')
options.add_argument('--incognito')
driver = webdriver.Chrome(executable_path=chromedriver_path+r'\chromedriver', options=options)
exclude = ['$', '.', ',']
LARGE_FONT= ("Verdana", 16)

def callback(url):
    webbrowser.open_new(url)

def alert_popup(title, message, url):
    root = tk.Tk()
    root.title(title)
    w = 500
    h = 200
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    w = tk.Label(root, text=message, width=120, height=3, font=LARGE_FONT)
    w.pack()
    link = tk.Label(root, text="Visit Store", height=2, fg="blue", cursor="hand2", font=LARGE_FONT)
    link.pack()
    link.bind("<Button-1>", lambda e: callback(url))
    b = tk.Button(root, text="OK", command=root.destroy, width=10)
    b.pack()
    tk.mainloop()


def get_page(url):
    global user_agent_list
    global driver
    global options
    for _ in range(1, 6):
        user_agent = random.choice(user_agent_list)
        headers = 'user-agent='+user_agent
        options.add_argument(headers)
        driver.get(url)
        src = driver.page_source
        soup = BeautifulSoup(src, features='html.parser')
        return soup
    return False

def get_ao_price(url):
    price_page = get_page(url)
    if price_page:
        span = price_page.find('span', {'class' : 'aol-product-price'})
        if span:
            price = span.text
            price = price.strip()
            price = ''.join(c for c in price if c not in exclude)
            return int(price)
        else:
            return False
    else:
        return False

def get_jbhifi_price(url):
    price_page = get_page(url)
    if price_page:
        span = price_page.find('span', {'class' : 'price'})
        if span:
            price = span.text
            price = price.strip()
            price = ''.join(c for c in price if c not in exclude)
            return int(price)
        else:
            return False
    else:
        return False

def get_ac_price(url):
    price_page = get_page(url)
    if price_page:
        span = price_page.find('div', {'class' : 'price'})
        if span:
            price = span.text
            price = price.strip()
            price = price[0:6]
            price = ''.join(c for c in price if c not in exclude)
            return int(price)
        else:
            return False
    else:
        return False

def get_videopro_price(url):
    price_page = get_page(url)
    if price_page:
        span = price_page.find('div', {'class' : 'product-price'})
        if span:
            price = span.text
            price = price.strip()
            price = ''.join(c for c in price if c not in exclude)
            return int(price)
        else:
            return False
    else:
        return False

def get_binglee_price(url):
    price_page = get_page(url)
    if price_page:
        span = price_page.find('span', {'class' : 'price'})
        if span:
            price = span.text
            price = price.strip()
            price = ''.join(c for c in price if c not in exclude)
            return int(price)
        else:
            return False
    else:
        return False

def get_harveynorman_price(url):
    price_page = get_page(url)
    if price_page:
        div = price_page.find('div', {'class' : 'product-view-sales'})
        span = div.find('span', {'class' : 'price'})
        if span:
            price = span.text
            price = price.strip()
            price = ''.join(c for c in price if c not in exclude)
            return int(price)
        else:
            return False
    else:
        return False

def get_thegoodguys_price(url):
    price_page = get_page(url)
    if price_page:
        span = price_page.find('span', {'class' : 'pricepoint-price'})
        if span:
            price = span.text
            price = price.strip()
            price = price[0:5]
            price = ''.join(c for c in price if c not in exclude)
            return int(price)
        else:
            return False
    else:
        return False



def get_prices():
    prices = {'Appliances Online':inf, 'JB-HiFi':inf, 'Appliance Central':inf, 'Videopro':inf, 'Bing Lee':inf, 'Harvey Norman':inf, 'The Good Guys':inf}

    price_ao = get_ao_price(ao)
    if price_ao and (price_ao < prices['Appliances Online']):
        prices['Appliances Online'] = price_ao

    price_jbhifi = get_jbhifi_price(jbhifi)
    if price_jbhifi and (price_jbhifi < prices['JB-HiFi']):
        prices['JB-HiFi'] = price_jbhifi

    price_ac = get_ac_price(ac)
    if price_ac and (price_ac < prices['Appliance Central']):
        prices['Appliance Central'] = price_ac

    price_videopro = get_videopro_price(videopro)
    if price_videopro and (price_videopro < prices['Videopro']):
        prices['Videopro'] = price_videopro

    price_binglee = get_binglee_price(binglee)
    if price_binglee and (price_binglee < prices['Bing Lee']):
        prices['Bing Lee'] = price_binglee

    price_harveynorman = get_harveynorman_price(harveynorman)
    if price_harveynorman and (price_harveynorman < prices['Harvey Norman']):
        prices['Harvey Norman'] = price_harveynorman

    price_thegoodguys = get_thegoodguys_price(thegoodguys)
    if price_thegoodguys and (price_thegoodguys < prices['The Good Guys']):
        prices['The Good Guys'] = price_thegoodguys

    sorted_prices = dict(sorted(prices.items(), key=lambda item: item[1]))
    
    return sorted_prices



