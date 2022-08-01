from lxml import etree
html = etree.parse('./xpath_test.html',etree.HTMLParser())
print('获取ul节点')
print(html.xpath('//ul'))
print(html.xpath('//li'))
print('根据属性选择')
print(html.xpath('//li[@class="item-inactive"]'))

print('获取节点下子节点')
print(html.xpath('//li[@class="item-inactive"]/a'))

print('获取节点文本')
print(html.xpath('//li[@class="item-inactive"]/a/text()'))

print('获取节点的属性值')
print(html.xpath('//li/a/@href'))
print(html.xpath('//li[@class="item-inactive"]/a/@href'))

print('多属性匹配')
text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
<li class="li" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
print(html.xpath('//li[@class="li li-first" and @name="item"]'))
print(html.xpath('//li[contains(@class,"li") and @name="item"]'))
