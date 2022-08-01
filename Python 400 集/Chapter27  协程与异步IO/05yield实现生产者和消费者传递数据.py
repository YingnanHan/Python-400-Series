def produce(c):
    for i in range(1,11):
        print('生产者生产产品:%d'%i)
        c.send(str(i))

def consumer():
    while True:
      res =  yield
      print('消费者消费产品：',res)

c = consumer()  #生成器对象
next(c)
produce(c)
