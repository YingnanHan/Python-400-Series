class Stack(object):
    #定义初始化方法
    def __init__(self):
        #初始化一个空列表
        self.__list=[]

    #压栈
    def push(self,item):
        self.__list.append(item)

    #弹出元素
    def pop(self):
        return self.__list.pop()

    #返回栈顶元素
    def peek(self):
        return self.__list[len(self.__list)-1]

    #判断栈是否为空
    def is_empty(self):
        return self.__list == []

    #计算栈的大小
    def size(self):
        return len(self.__list)

if __name__ == '__main__':
    stack=Stack()
    print('是否空栈吗',stack.is_empty())
    #压栈
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print('是否空栈吗', stack.is_empty())
    print('栈的长度：',stack.size())
    #弹出
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())