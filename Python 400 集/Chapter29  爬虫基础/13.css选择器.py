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
# print(soup.select('.panel'))
print(soup.select('.panel .panel-heading'))
print(soup.select('#list-2'))
for ul in soup.select('#list-2'):
    for li in ul.find_all('li'):
        print('string:',li.string)
        print('text:',li.text)
        print('get_text():',li.get_text())