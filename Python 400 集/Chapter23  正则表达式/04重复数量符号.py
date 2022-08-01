'''
* :0次或多次
?:0次或1次
+:至少1次
{m}:重复m次
{m,n}:重复m到n次
{m}：至少重复m次
'''
import re
print('--------*的使用------------')
pattern='\d*'
s='123qwe'
s='123456qwe'
s='qwe'
o=re.match(pattern,s)
print(o)

print('--------+的使用------------')
pattern='\d+'
# s='123qwe'
# s='1qwe'
# s='123456qwe'
s='qwe'
o=re.match(pattern,s)
print(o)

print('--------?的使用------------')
pattern='\d?'
s='123qwe'
s='1qwe'
s='123456qwe'
s='qwe'
o=re.match(pattern,s)
print(o)

print('---------{m}-----------')
pattern='\d{2}'
pattern='\d{3}'
pattern='\d{4}'
s='123qwe'
o=re.match(pattern,s)
print(o)

print('---------{m,n}-----------')
pattern='\d{2,5}'
s='123qwe'
s='123456qwe'
s='qwe'
o=re.match(pattern,s)
print(o)

print('---------{m,}-----------')
pattern='\d{2,}'
s='123qwe'
s='123456qwe'
s='qwe'
o=re.match(pattern,s)
print(o)