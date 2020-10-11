import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from scipy import stats
import numpy as np
import urllib.request
import os
# urllib.request.urlretrieve("http://www.gunnerkrigg.com//comics/00000001.jpg", "00000001.jpg")

item_name = []
prices = []
links = []
images_links = []

for i in range(4):

    ebayUrl = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=cricket+bats&_sacat=0&LH_TitleDesc=0&_pgn="+str(i)
    # ebayUrl = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=iphone&_sacat=0&LH_TitleDesc=0&LH_PrefLoc=2&LH_Complete=1&LH_Sold=1&_pgn="+str(i)
    print(ebayUrl)
    r = requests.get(ebayUrl)
    data = r.text
    soup = BeautifulSoup(data,features="lxml")
    listings = soup.find_all('li', attrs={'class': "s-item"})
    print(listings)
#     for listing in listings:
#         prod_name = " "
#         prod_price = " "
#         for name in listing.find_all('h3', attrs={'class': "s-item__title"}):
#             if (str(name.find(text=True, recursive=False)) != "None"):
#                 prod_name = str(name.find(text=True, recursive=False))
#                 print(prod_name)
#                 item_name.append(prod_name)
#
#         if (prod_name != " "):
#             price = listing.find('span', attrs={'class': "s-item__price"})
#             if price.find_all('span', attrs={'class': "POSITIVE"}) != []:
#                 price = price.find('span', attrs={'class': "POSITIVE"})
#             prod_price = str(price.find(text=True, recursive=False))
#             prod_price = float(re.sub(",", "", prod_price.split("INR")[1])) #.split(".")[0]))
#             prices.append(prod_price)
#
#             l = listing.find('div', attrs={'class': "s-item__info clearfix"})
#             link = l.find('a')['href']
#             links.append(link)
#
# cricket_bats = pd.DataFrame({"Name": item_name, "Prices": prices, "Links":links})
# print(cricket_bats)
# cricket_bats.to_csv('EBayCricketBatPricesOn24thAugust2020.csv',index=False)
#
# if not os.path.exists('C:/Users/mehra/OneDrive/Documents/GitHub/ML-Portfolio-Marketplace-Scraping/images'):
#     os.makedirs('C:/Users/mehra/OneDrive/Documents/GitHub/ML-Portfolio-Marketplace-Scraping/images')
#
# # Download all images for all listings for a particular search result
# for link in links:
#     r1 = requests.get(link)
#     data1 = r1.text
#     soup1 = BeautifulSoup(data1, features="lxml")
#     print(link)
#     if soup1.find_all('img', attrs={'id':'icImg'}) != []:
#         n = soup1.find_all('img', attrs={'id':'icImg'})[0]['src']
#         img_name = n.split('/')[-2] + '.jpg'
#         urllib.request.urlretrieve(n, 'images/' + img_name)



