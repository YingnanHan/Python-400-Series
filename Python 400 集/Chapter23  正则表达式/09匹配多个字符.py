import re
pattern='aa|bb|cc'
s='aa'
o=re.match(pattern,s)
print(o)

s='bb'
o=re.match(pattern,s)
print(o)

s='my name is cc'
o=re.search(pattern,s)
o=re.match(pattern,s)
print(o)
print('匹配0-100之间所有的数字')
#匹配0-100之间所有的数字  0-99|100
pattern=r'[1-9]?\d$|100$'
s='1'
s='11'
s='99'
s='100'
s='1000'
o=re.match(pattern,s)
print(o)