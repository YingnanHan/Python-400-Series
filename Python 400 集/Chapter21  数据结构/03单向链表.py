class Node(object):
    def __init__(self,elem):
        #elem指数据元素
        self.elem=elem
        #指向下一个节点的链接域
        self.next=None

#构造单向链表类
class SingleLinkList:
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
        #将新节点的链接域next指向头节点
        node.next=self.__head
        #将链表的头__head指向新节点
        self.__head=node
    #在单向链表尾部追加元素
    def append(self,item):
        #将传入的值构造成节点
        node=Node(item)
        if self.is_empty():#单链表为空时候
            self.__head=node
        else: #单链表不为空
            curNode=self.__head
            while curNode.next!=None:
                curNode=curNode.next
            #修改节点指向  最后一个节点的next指向node
            curNode.next=node
    #在指定位置添加元素
    def insert(self,pos,item):
        #如果传入的pos是小于等于0的数，默认的将节点插入头部
        if pos<=0:
            self.add(item)
        #如果pos的值大于链表长度，直接将节点添加到尾部
        elif pos> (self.length()-1):
            self.append(item)
        else:
            #构造节点
            node=Node(item)
            count=0
            preNode=self.__head
            while count<(pos-1): #找前一个节点
                count+=1
                preNode=preNode.next
            #修改指向
            #将前一个节点的next指向插入位置节点
            node.next=preNode.next
            #将插入位置的前一个节点的next指向新节点
            preNode.next=node


    #删除节点
    def remove(self,item):
        curNode=self.__head
        preNode=None
        while curNode !=None:
            if curNode.elem == item:
                #判断是否是头节点
                if preNode == None :#是头节点
                    self.__head=curNode.next
                else:
                    #删除
                    preNode.next=curNode.next
                break
            else:
                preNode=curNode
                curNode=curNode.next
    #查找节点是否存在
    def search(self,item):
        curNode=self.__head
        while curNode != None:
            if curNode.elem == item:
                return True
            curNode=curNode.next
        return False
    #判断单向链表是否为空
    def is_empty(self):
        #判断head指向是None，如果是None则就是空链表
        # if self.__head == None:
        #     return True
        # else:
        #     return False
        return self.__head == None

    #计算单向链表的长度
    def length(self):
        count=0
        curNode=self.__head
        while curNode !=None:
            count+=1
            curNode=curNode.next
        return count
    def travel(self):
        curNode=self.__head
        while curNode!=None:
            print(curNode.elem,end='\t')
            curNode=curNode.next
        print("")

if __name__ == '__main__':
    #初始化元素值为20的单向链表
    # singleLinkList=SingleLinkList(20)
    #初始化一个空的单向链表
    singleLinkList=SingleLinkList()
    print('是否是空链表：',singleLinkList.is_empty())
    print('链表的长度：',singleLinkList.length())
    print('----------遍历单链表----------')
    singleLinkList.travel()
    print('--------查找---------')
    print(singleLinkList.search(20))
    print(singleLinkList.search(30))
    print('------头部插入-----------')
    singleLinkList.add(1)
    singleLinkList.add(2)
    singleLinkList.add(3)
    singleLinkList.travel()
    print('------尾部追加-----------')
    singleLinkList.append(10)
    singleLinkList.append(20)
    singleLinkList.append(30)
    singleLinkList.travel()
    print('链表的长度：', singleLinkList.length())
    print('----------指定位置插入----------')
    singleLinkList.insert(2,100)
    singleLinkList.travel()
    singleLinkList.insert(-1, 200)
    singleLinkList.travel()
    singleLinkList.insert(100, 300)
    singleLinkList.travel()
    print('---------删除节点--------')
    singleLinkList.remove(100)
    singleLinkList.travel()
    singleLinkList.remove(200)
    singleLinkList.travel()
    singleLinkList.remove(300)
    singleLinkList.travel()