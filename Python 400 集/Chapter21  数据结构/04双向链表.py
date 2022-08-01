#双向链表的节点
class Node:
    def __init__(self,elem):
        self.elem=elem
        self.next=None #后继 下一个节点
        self.prev=None  #前驱  前一个节点

class DoubleLinkList:
    #初始化方法
    def __init__(self,node=None):
        #判断node是否为空
        if node !=None:
            headNode=Node(node)
            self.__head=headNode
        else:
            self.__head=node

    #在头部添加元素
    def add(self,item):
        #将传入的值构造成节点
        node=Node(item)
        #判断是否是空链表
        if self.is_empty():
            self.__head=node
        else:
            #将新节点的链接域next指向头节点
            node.next=self.__head
            #将__head的头节点的prev指向node
            self.__head.prev=node
            #将链表的头__head指向新节点
            self.__head=node
    #在尾部追加元素
    def append(self,item):
        #将传入的值构造成节点
        node=Node(item)
        if self.is_empty():#单链表为空时候
            self.__head=node
        else: #不为空
            curNode=self.__head
            while curNode.next!=None:
                curNode=curNode.next
            #修改节点指向  最后一个节点的next指向node
            curNode.next=node
            #将node节点的前驱指向当前节点
            node.prev=curNode
    #在指定位置添加元素
    def insert(self,pos,item):
        # 如果传入的pos是小于等于0的数，默认的将节点插入头部
        if pos <= 0:
            self.add(item)
        # 如果pos的值大于链表长度，直接将节点添加到尾部
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            # 构造节点
            node = Node(item)
            count = 0
            curNode = self.__head
            while count < (pos - 1):  # 找前一个节点
                count += 1
                curNode = curNode.next
            # 修改指向
            #将node节点的前驱指向当前节点
            node.prev = curNode
            #将node节点的后继指向当前节点的下一个节点
            node.next = curNode.next
            #将当前节点的下一个节点的前驱指向node节点
            curNode.next.prev = node
            #将当前节点的后继指向node节点
            curNode.next = node

    #删除节点
    def remove(self,item):
        curNode=self.__head
        while curNode !=None:
            if curNode.elem == item:
                #判断是否是头节点
                if curNode ==self.__head :#是头节点
                    self.__head=curNode.next
                    #判断当前节点是否只有一个节点，如果只有一个节点，则不需要移动下一个节点的前驱
                    if curNode.next:
                        curNode.next.prev=None
                else:
                    #删除
                    curNode.prev.next = curNode.next
                    #判断当前节点是否是最后一个节点，如果是最后一个节点，最后一个节点的下一个节点指向None
                    if curNode.next:
                        curNode.next.prev = curNode.prev
                break
            else:
                curNode=curNode.next
    #查找节点是否存在
    def search(self,item):
        curNode=self.__head
        while curNode != None:
            if curNode.elem == item:
                return True
            curNode=curNode.next
        return False
    #判断是否为空
    def is_empty(self):
        #判断head指向是None，如果是None则就是空链表
        # if self.__head == None:
        #     return True
        # else:
        #     return False
        return self.__head == None

    #计算链表的长度
    def length(self):
        count=0
        curNode=self.__head
        while curNode !=None:
            count+=1
            curNode=curNode.next
        return count
    #遍历链表
    def travel(self):
        curNode=self.__head
        while curNode!=None:
            print(curNode.elem,end='\t')
            curNode=curNode.next
        print("")

if __name__ == '__main__':
    doubleLinkList=DoubleLinkList()
    doubleLinkList.add(11)
    doubleLinkList.add(22)
    doubleLinkList.add(33)
    doubleLinkList.travel()
    print('-----------追加-----------')
    doubleLinkList.append(100)
    doubleLinkList.append(200)
    doubleLinkList.append(300)
    doubleLinkList.travel()
    print('指定位置插入')
    doubleLinkList.insert(-1,44)
    doubleLinkList.travel()
    doubleLinkList.insert(100,400)
    doubleLinkList.travel()
    doubleLinkList.insert(2,1000)
    doubleLinkList.travel()
    print('------删除节点--------')
    doubleLinkList.remove(44)
    doubleLinkList.travel()
    doubleLinkList.remove(1000)
    doubleLinkList.travel()
    doubleLinkList.remove(400)
    doubleLinkList.travel()
    print('链表的长度：',doubleLinkList.length())
    print('查找节点11',doubleLinkList.search(11))
    print('查找节点111',doubleLinkList.search(111))
