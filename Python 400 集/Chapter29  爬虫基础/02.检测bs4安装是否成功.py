from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>段落标签</p>','html.parser')
print(soup.p.string)
