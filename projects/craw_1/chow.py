from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import html2text
import requests
import lxml

url = 'https://www.zhouxingchifans.com/t66.html'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

r = requests.get(url, headers=headers, verify=False)

# doc = pq(r.text)
# content = doc(".content").html()
# content = html2text.html2text(content)

soup = BeautifulSoup(r.text, 'lxml')
content = soup.find(class_='content')
content = html2text.html2text(str(content))

with open('chow.txt', 'w', encoding='utf-8') as f:
    f.write(content)
