from time import sleep
#一个失败的模拟
def sing():
    for i in range(3):
        print("正在唱歌...%d"%i)
        sleep(1)
        dance()

def dance():
    for i in range(3):
        print("正在跳舞...%d"%i)
        sleep(1)
        sing()

if __name__ == '__main__':
    sing()
