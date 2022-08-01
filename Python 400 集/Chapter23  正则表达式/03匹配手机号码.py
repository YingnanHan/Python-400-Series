import re
# pattern='\d\d\d\d\d\d\d\d\d\d\d'
pattern='1[35789]\d\d\d\d\d\d\d\d\d'
s='13456788765'
o=re.match(pattern,s)
print(o)

#电话号码   区号-座机号  010-3762266   0342-8776262