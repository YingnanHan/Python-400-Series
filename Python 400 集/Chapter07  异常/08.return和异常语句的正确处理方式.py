def test01():
    print("step01")
    try:
        x = 3 / 0
        # return "a"
    except:
        print("step02")
        print("异常：除数不能为0")
        # return "b"
    finally:
        print("step03")
        # return "c"

    print("step05")
    return "e"


# 一般不要将return语句放到try,except,else,finally块中，会发生一些意想不到的错误
# 建议放到方法的最后
print(test01())
