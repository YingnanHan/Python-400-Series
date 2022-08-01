import re
s='hello python'
pattern='hello'
o=re.match(pattern,s)
print(o)
print(dir(o))
print(o.group()) #返回匹配的字符串
print(o.span())
print(o.start())
print('flags参数的使用')
s='hello python'
pattern='Hello'
o=re.match(pattern,s,flags=re.I)
print(o)
print(o.group())