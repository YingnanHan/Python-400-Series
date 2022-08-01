import re
print('--------sub-------------')
phone='2004-959-559 # 这是一个国外电话号码'
#将phone中的注释去掉
pattern=r'#.*$'
result=re.sub(pattern,'',phone)
print('sub:',result)
pattern=r'#\D*'
result=re.sub(pattern,'',phone)
print('sub:',result)
print('---------subn-----------')
result=re.subn(pattern,'',phone)
print(result)
print(result[0])
print(result[1])
print('---------compile------------')
s='first123 line'
pattern=r'\w+'
regex=re.compile(pattern)
o=regex.match(s)
print(o)
print('---------findall-------------')
s='first 1 second 2 third 3'
pattern=r'\w+'
result=re.findall(pattern,s)
print(result)
print('---------finditer-------------')
s='first 1 second 2 third 3'
pattern=r'\w+'
result=re.finditer(pattern,s)
print(result)
for i in result:
    print(i.group(),end='\t')
print()
print('----------split-------------')
s='first 11 second 22 third 33'
pattern=r'\d+'
result=re.split(pattern,s)
print(result)
result=re.split(pattern,s,maxsplit=2)
print(result)

