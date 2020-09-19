import bs4 as bs
import requests
import pandas as pd

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36' }
url = 'https://www.englishdom.com/blog/1000-samyx-vazhnyx-slov-v-anglijskom-yazyke/'

d=pd.read_html(url)
print(d[0][1][0])

with open('RushenWord1.txt', 'w+') as a:
    for i in d[0][2]:
        a.writelines(i+'\n')

with open('englishWord1.txt', 'w+') as a:
    for i in d[0][1]:
        a.writelines(i+'\n')