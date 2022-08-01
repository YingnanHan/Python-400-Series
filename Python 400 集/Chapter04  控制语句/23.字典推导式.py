# 统计文本中不同字符出现的字数
test = "The English text distributed at this meeting noted that the OSCE had 'aided' Georgia during certain serious incidents.\
"
char_count = {c: test.count(c) for c in test}
print(char_count)
