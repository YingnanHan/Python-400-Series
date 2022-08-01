import re
v = re.match(r'(.+)(\d+-\d+-\d+)','This is my tel:133-1234-1234')
print('----------贪婪模式---------')
print(v.group(1))
print(v.group(2))
print('----------非贪婪模式---------')
v = re.match(r'(.+?)(\d+-\d+-\d+)','This is my tel:133-1234-1234')
print(v.group(1))
print(v.group(2))
print('-------实例2--------')
print('贪婪模式')
v= re.match(r'abc(\d+)','abc123')
print(v.group(1)) #123
#非贪婪模式
print('非贪婪模式')
v= re.match(r'abc(\d+?)','abc123')
print(v.group(1)) #1