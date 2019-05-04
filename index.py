import requests
import bs4

res = requests.get('https://tonyciccarone.com')
soup = bs4.BeautifulSoup(res.text, 'lxml')
