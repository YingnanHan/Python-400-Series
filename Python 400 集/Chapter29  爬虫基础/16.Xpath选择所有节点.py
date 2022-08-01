from lxml import etree
html = etree.parse('./xpath_test.html',etree.HTMLParser())
result = html.xpath('//*') #获取所有节点
print(result)