'''
同步：先执行第一个事务，如果遇到阻塞(time.sleep())，会一直等待，直到第一个事务执行完毕，
     才会执行第二事务

异步：与同步是相对的，指执行第一个事务时候，如果遇到阻塞，会直接执行第二个事务，不会等待
      通过状态、通知、回调来调用处理结果
'''
import time
now = lambda: time.time()
def foo():
    time.sleep(1)

start = now()
for i in range(5):
    foo()
print('同步所花费的时间：',(now()-start))

print('协程实现异步')
import asyncio
async def foo():
    asyncio.sleep(1)
start = now()
loop = asyncio.get_event_loop()
for i in range(5):
    loop.run_until_complete(foo())
print('异步所花费的时间:',(now()-start))