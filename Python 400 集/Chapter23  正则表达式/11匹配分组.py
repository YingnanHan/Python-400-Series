'''
(ab)	将括号中的字符作为一个分组
\num	引用分组num匹配到的字符串
(?p<name>)	分别起组名
(?p=name)	引用别名为name分组匹配到的字符串
'''
import re
print('匹配座机号码')
#匹配座机号码 区号{3,4}-电话号码{5,8}  010-43222   0432-447727
pattern=r'\d{3,4}-[1-9]\d{4,7}$'
pattern=r'(\d{3,4})-([1-9]\d{4,7}$)'
s='010-786545'
o=re.match(pattern,s)
print(o)
print(o.group())
print(o.group(1))
print(o.group(2))
# print(o.groups())
# print(o.groups()[0])
# print(o.groups()[1])
print('匹配出网页标签内的数据')
# pattern=r'<.+><.+>.+</.+></.+>'
pattern=r'<(.+)><(.+)>.+</\2></\1>'
# s='<html><head>head部分</head></html>'
s='<html><title>head部分</head></body>'
o=re.match(pattern,s)
print(o)
#<body><h1><div><div></div></div></h1></body>
print('(?P<name>)	分别起组名')
pattern=r'<(?P<k_html>.+)><(?P<k_head>.+)>.+</(?P=k_head)></(?P=k_html)>'
s='<html><head>head部分</head></html>'
s='<html><title>head部分</head></body>'
o=re.match(pattern,s)
print(o)

