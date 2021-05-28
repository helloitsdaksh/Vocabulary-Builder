from  bs4 import BeautifulSoup
import requests
import pandas as pd

words = []
meaning = []
agent = {"User-Agent":"Mozilla/5.0"}
source  = requests.get("https://www.graduateshotline.com/gre-word-list.html",headers = agent).text
soup = BeautifulSoup(source,'lxml')
new_soup = soup.find('table',class_ = 'tablex border1')
for article in new_soup.find_all('tr'):
    count = 0
    for i in article.find_all('td'):
        if count == 0:
            words.append(i.text)
            count +=1
        elif count == 1:
            meaning.append(i.text)
print(words)

