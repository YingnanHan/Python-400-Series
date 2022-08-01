import re
#匹配QQ邮箱  5-10位数字
qq='8656707@qq.com'
qq='8656707@qq.com.cn'
qq='8656707@qq.com.126.com'
# pattern='[1-9]\d{4,9}@qq.com'
pattern=r'[1-9]\d{4,9}@qq.com$'
o=re.match(pattern,qq)
print(o)
print('----------^开始------------')
# s='hello world'
s='hello python'
s='hepython'
pattern=r'^hello.*'
o=re.match(pattern,s)
print(o)
print('-------\\b匹配单词的左边界------------')
pattern=r'.*\bab'
s='12345 abc'
o=re.match(pattern,s)
print(o)
print('-------\\b匹配单词的右边界------------')
pattern=r'.*ab\b'
s='12345 abc'
s='12345 ab'
o=re.match(pattern,s)
print(o)
print('-------\\B匹配非单词的边界------------')
pattern=r'.*ab\B'
s='12345 abc'
s='12345 ab'
o=re.match(pattern,s)
print(o)
