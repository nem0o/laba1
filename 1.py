import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent as ua


url = 'https://omsk.cian.ru/kupit-kvartiru-1-komn-ili-2-komn/'

response = requests.get(url, headers={'User-Agent': ua().chrome})
soup = bs(response.content,'html.parser')

divs = soup.find_all('div', attrs={'class': '_93444fe79c--container--kZeLu _93444fe79c--link--DqDOy'})
for div in divs.find_all('a', href=True):
    name = div['href']
    print("Найдена ссылка:", name)
