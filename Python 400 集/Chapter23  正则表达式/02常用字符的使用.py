'''
.	匹配任意一个字符（除了\n）
[]	匹配列表中的字符
\w	匹配字母、数字、下划线，即a-z,A-Z,0-9,_
\W	匹配不是字母、数字、下划线
\s	匹配空白字符,即空格（\n,\t）
\S	匹配不是空白的字符
\d	匹配数字,即0-9
\D	匹配非数字的字符
'''
import re
print('--------.的使用--------')
s='a'
s='A'
s='8'
s='_'
s='\n'
pattern='.'
o=re.match(pattern,s)
print(o)
print('---------\d的使用------------')
s='0'
s='5'
s='9'
s='a'
pattern='\d'
o=re.match(pattern,s)
print(o)
print('---------\D的使用------------')
s='0'
# s='5'
s='9'
s='a'
pattern='\D'
o=re.match(pattern,s)
print(o)
print('--------\s的使用-----------')
s=' '
s='\n'
s='\t'
s='_'
pattern='\s'
o=re.match(pattern,s)
print(o)
print('--------\S的使用-----------')
s=' '
s='\n'
s='\t'
s='_'
pattern='\S'
o=re.match(pattern,s)
print(o)
print('---------\w的使用------------')
s='z'
s='A'
s='8'
s='_'
s='#'
pattern='\w'
o=re.match(pattern,s)
print(o)

print('---------\W的使用------------')
s='z'
# s='A'
s='8'
s='_'
s='#'
s='+'
pattern='\W'
o=re.match(pattern,s)
print(o)
print('---------[]的使用----------')
pattern='[2468]'
s='2'
s='3'
s='4'
s='6'
# s='8'
o=re.match(pattern,s)
print(o)