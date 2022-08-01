import re
pattern='hello'
s='hello python'
# m=re.search(pattern,s)
m=re.match(pattern,s)
print(m)
print(m.group())
print('-------macth和search的区别----------')
pattern='love'
s='I love you'
m=re.match(pattern,s)
print('使用match进行匹配',m)
o=re.search(pattern,s)
print('使用search进行匹配',o)