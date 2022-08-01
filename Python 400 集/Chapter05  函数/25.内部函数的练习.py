# 以打印中国人与外国人的名字为例
def printName(isChiese, name, familyname):
    def inner(a, b):
        print("{0} {1}".format(a, b))

    if isChiese:
        inner(familyname, name)
    else:
        inner(name, familyname)


printName(True, "Lei", "Li")
