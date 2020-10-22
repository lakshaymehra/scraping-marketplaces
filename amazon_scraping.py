import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


item_name = []
prices = []


for i in range(4):

    amazonUrl = "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_2?ie=UTF8&pg="+str(i)
    r = requests.get(amazonUrl)
    data = r.text
    soup = BeautifulSoup(data,features="lxml")
    # print(soup)
    listings = soup.find_all('div', attrs={'class': 'a-section a-spacing-none aok-relative'})
    # print(listings)
    for listing in listings:
        prod_name = " "
        prod_price = " "
        n = listing.find('span', attrs={'class': "zg-text-center-align"})
        na = n.find('div', attrs={'class': "a-section a-spacing-small"})
        # print(na)
        prod_name = na.find_all('img', alt=True)[0]['alt']
        # print(prod_name)
        item_name.append(prod_name)
        prod_price = "INR " + listing.find('span',attrs={'class':'p13n-sc-price'}).text[2:]
        # print(prod_price)
        prices.append(prod_price)

books = pd.DataFrame({"Name": item_name, "Prices": prices})
print(books)
books.to_csv('Amazon_Best_Selling_Books_On_{}.csv'.format(datetime.today().strftime('%Y-%m-%d')),index=False)