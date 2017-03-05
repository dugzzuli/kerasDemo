from bs4 import BeautifulSoup
from urllib.request import urlopen
html=urlopen("http://www.baidu.com")
bs=BeautifulSoup(html.read())
print(bs.title)

