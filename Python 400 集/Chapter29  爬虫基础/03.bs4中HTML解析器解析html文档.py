from bs4 import BeautifulSoup
soup = BeautifulSoup('<h2>标题</h2>','lxml')
print(soup.h2.string)