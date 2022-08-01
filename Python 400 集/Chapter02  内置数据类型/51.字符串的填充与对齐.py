# 填充经常与对齐一同使用，
# ^ < >分别是居中，左对齐，以及右对齐，后面的数字是宽度
#:号后面带填充字符，只能是一个字符，不指定的话默认使用空格填充
print("My{0: <8}name{1: ^8}is{2: >8}".format("full", "Nick", "fake name"))
print("My{0:/<8}name{1:*^8}is{2:$>8}".format("full", "Nick", "fake name"))
