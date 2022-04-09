# scraper.py
import requests
from bs4 import BeautifulSoup
url = 'https://www.chemicalaid.com/tools/oxidationnumber.php?compound='+input("Вещество:")
response = requests.get(url,headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.119 YaBrowser/22.3.0.2430 Yowser/2.5 Safari/537.36"})
soup = BeautifulSoup(response.text, 'lxml')
if soup!=0:
    print("HTML confirmed")
quotes = soup.find_all('p', class_='text-center lead mt-2 px-2')

print(quotes)
for link in soup.find('p'):
    print(link)