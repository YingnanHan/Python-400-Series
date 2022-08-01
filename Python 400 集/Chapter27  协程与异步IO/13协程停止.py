import time,asyncio
async def do_work(x):
    print('waitting:',x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

#创建协程对象
coroutine1 = do_work(1)
coroutine2 = do_work(2)
coroutine3 = do_work(4)

#创建任务列表
tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]
start = time.time()
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:
    #获取事件循环中所有任务列表
    # print(asyncio.Task.all_tasks())
    for task in asyncio.Task.all_tasks():
        print(task.cancel()) #如果返回的True代表当前任务取消成功
    loop.stop()
    loop.run_forever()
finally:
    loop.close()
print('TIME:',time.time()-start)
