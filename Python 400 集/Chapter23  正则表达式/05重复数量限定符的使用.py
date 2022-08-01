import re
print('------案例1------')
#匹配出一个字符串首字母为大写字符，后边都是小写字符，这些小写字母可有可无
pattern='[A-Z][a-z]*'
s='Hello'
s='HEllo'
o=re.match(pattern,s)
print(o)

print('------案例2------')
#匹配出有效的变量名 （字母 、数字 下划线 ，而且数字不能开头）
# pattern='[a-zA-Z_][a-zA-Z0-9_]*'
pattern='[a-zA-Z_]\w*'
s='userName'
s='age'
s='a'
s='_qwe'
# s='3er'
o=re.match(pattern,s)
print(o)
print('-------案例3----------')
#匹配出1-99直接的数字
pattern='[1-9]\d?'
s='2'
s='99'
s='100'
s='0'
o=re.match(pattern,s)
print(o)
print('----------案例4--------------')
#匹配出一个随机密码8-20位以内  (大写字母 小写字母 下划线 数字)
pattern='\w{8,20}'
s='123456789'
s='abc123qwe_'
s='1234567#'
o=re.match(pattern,s)
print(o)