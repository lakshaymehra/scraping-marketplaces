import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import shutil


solutions = []
links = []

# kal_url = "http://www.users.on.net/~mikegatley/kaleidoscope/all1.html"
kal_url = "http://www.users.on.net/~mikegatley/kaleidoscope/multi.html"
r = requests.get(kal_url)
data = r.text
soup = BeautifulSoup(data,features="lxml")
listings = soup.find_all('img')

for listing in listings:
    link = listing['src']
    if link[-4:] != '.gif':
        continue
    solution_link = link.replace('Small', 'Solution')
    link = link.replace('Small','')
    solutions.append(solution_link)
    links.append(link)

print(links)
print(solutions)
#
# if os.path.exists('C:/Users/mehra/OneDrive/Documents/GitHub/scraping-marketplaces/patterns'):
#     shutil.rmtree('C:/Users/mehra/OneDrive/Documents/GitHub/scraping-marketplaces/patterns')
#
os.makedirs('C:/Users/mehra/OneDrive/Documents/GitHub/scraping-marketplaces/multi')
#
#
# if os.path.exists('C:/Users/mehra/OneDrive/Documents/GitHub/scraping-marketplaces/solutions'):
#     shutil.rmtree('C:/Users/mehra/OneDrive/Documents/GitHub/scraping-marketplaces/solutions')
#
# os.makedirs('C:/Users/mehra/OneDrive/Documents/GitHub/scraping-marketplaces/solutions')


# Download all patterns
for link in links:
    img_name = link.split('/')[-1][2:-4] + '.jpg'
    urllib.request.urlretrieve(link, 'multi/' + img_name)

# Download all solutions
for link in solutions:
    img_name = link.split('/')[-1][2:-4] + '.jpg'
    urllib.request.urlretrieve(link, 'multi/' + img_name)