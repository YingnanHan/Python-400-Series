import time,asyncio
async def do_work(x):
    print('waitting:',x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

async def main():
    # 创建协程对象
    coroutine1 = do_work(1)
    coroutine2 = do_work(2)
    coroutine3 = do_work(4)

    # 创建任务列表
    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
    dones,pending = await asyncio.wait(tasks)
    for task in dones:
        print('Task ret:',task.result())
start = time.time()
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(main())
try:
    loop.run_until_complete(task)
except KeyboardInterrupt as e:
    #获取事件循环中所有任务列表
    # print(asyncio.Task.all_tasks())
    print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()
print('TIME:',time.time()-start)
