import selenium
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
l = []

browser = webdriver.Chrome('C:/chromedriver.exe')

site = browser.get("https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
s= browser.page_source
print(s)

# x = requests.get('https://en.wikipedia.org/wiki/List_of_highest-grossing_films')

# with open('main.html','wb') as f:
#     f.write(x.content)



# with open('main.html','r', encoding="utf-8") as html_file: 
#     soup = bs(html_file,'html5lib')
# table = soup.find('tbody')
# content = table.find_all("tr")


# for row in content[1:]:
#     name = row.find("a").text
#     t = row.findAll("td")
#     gross = int(t[2].text.replace("\n", "").replace(",","").split("$")[1])
#     year = int(t[3].text.replace("\n", ""))
#     l.append((name, gross, year))

# # for i in l:
# #     print(i) 

# x= pd.DataFrame(data=l, columns=("Movie","Gross","Year"))
# # print(x.head())
# x.to_csv('highest-grossing-film.csv')

# print(f'{name} earned revenue of {gross} dollars!')

# print(x.info())
# print(soup.prettify())

# match = soup.title
# print(match)







# soup = bs(x.page_source)
# print(soup.prettify())