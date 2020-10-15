#                           DISCLAIMER

# I'v tried to do the project with amazon.com but It wouldn't even let me get the simplest css_selectors

# Even though the html I would recieve was the right html(I checked it in an html viewer),after I use BeautifulSoup on it,the only things I can get from it are 26 divs

# all the divs are the same thing and their text is a warning saying I cant use this method for accessing amazon.com

# I tried fake-headers,giving it one of the famous or even giving it 24 hours rest and trying again the next day but nothing changed

# So I did the project on another site called bookdepository.com beacuse it's very similar to amazon,still needs a good header to access it and shows the title and the author the same way as amazon

# It also different payment systems(such as paperback and hardcopy and ...)just like amazon and when a book goes on sale,it shows it just like amazon does

# So I could do the entire project on this site while showing that I possess all the programing skills needed for this project

# I hope you can understand my problem and judge my project accordingly

# with regards

# peiman razavi



import requests
import re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
agent=ua.chrome
url='https://www.bookdepository.com/search?searchTerm='+input('enter the serach term for the book: ').replace(' ','+')+'&search=Find+book'
css_selector='.title a'
css_selector2='.author span a'
css_selector3='.item-info'
headers = {'User-Agent': f'{agent}'}
request=requests.get(url,headers=headers)
soup=BeautifulSoup(request.text,'html.parser')
title=soup.select(css_selector)
author=soup.select(css_selector2)
info=soup.select(css_selector3)
books={}
cheapest_book={}
for i in range(len(title)):
    # %(i+1)  is added as a counter to avoid removing books with similar titles.
    books['%dth one is '%(i+1)+(title[i].get_text()).strip()]=(author[i].get_text()).strip()
print(books)
price=100000000
cheapest=''
for i in info:
    grouped=(i.get_text()).split('\n')
    for k in grouped:
        if k.find('Paperback') != -1:
            for j in grouped:
                if j.find('US') != -1:
                    cost=float((re.sub(r'US\$','',j)).strip())
                    if price > cost :
                        price=cost
                        cheapest=grouped[3].strip()
                    break
            break
cheapest_book[cheapest]=price
print(cheapest_book)