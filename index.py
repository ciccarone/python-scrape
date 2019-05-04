import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Web_development')
soup = bs4.BeautifulSoup(res.text, 'lxml')


for i in soup.select('.toc ul li a'):
    print(i.text)