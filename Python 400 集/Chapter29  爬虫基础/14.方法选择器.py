html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
# print(soup.find_all(name='ul'))
for ul in soup.find_all(name='ul'):
    for li in ul.find_all(name='li'):
        print(li.string)

print('属性参数attrs')
print(soup.find_all(name='ul',attrs={'id':'list-1'}))
print(soup.find_all(attrs={'id':'list-2'}))
print(soup.find_all(id='list-2'))
print('class_属性')
print(soup.find_all(class_='list'))
print('text参数')
import re
print(soup.find_all(text=re.compile('Foo')))
print('find()匹配到第一个元素')
print(soup.find(class_='list'))

