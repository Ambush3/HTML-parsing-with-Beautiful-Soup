import requests
from bs4 import BeautifulSoup

path= 'https://www.reddit.com/r/Programming/'
headers ={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}
with requests.Session() as s:
    r = s.get(path, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")
    threads = soup.select('a.title.may-blank')
    for a in threads:
        print(a)




