import asyncio,time
async def do_work(x):
    print('waitting :',x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

start = time.time()
#创建协程对象
coroutine = do_work(3)
#创建事件循环
loop = asyncio.get_event_loop()
#创建任务
task = asyncio.ensure_future(coroutine)
#执行任务
loop.run_until_complete(task)
#获取返回的结果
print('Task result:',task.result())
print('TIME:',time.time()-start)