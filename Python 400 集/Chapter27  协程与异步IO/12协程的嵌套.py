import time ,asyncio
async def do_work(x):
    print('waiting:',x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

async def main():
    #创建多个协程对象
    #封装任务列表
    coroutine1 = do_work(1)
    coroutine2 = do_work(2)
    coroutine3 = do_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    #1.获取返回结果的方式
    # dones,pendings = await asyncio.wait(tasks)
    # for task in dones:
    #     print('Task 返回结果：',task.result())

    #2获取返回结果的方式
    # results = await asyncio.gather(*tasks)
    # for result in results:
    #     print('Task 返回结果：',result)

    #3获取返回结果
    # return await asyncio.gather(*tasks)

    # #4.获取返回结果
    # return await asyncio.wait(tasks)

    ##5.获取返回结果
    for task in asyncio.as_completed(tasks):
        result = await task
        print('Task result:{}'.format(result))
start = time.time()
#将main协程对象加入到事件循环中
loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

#3种获取返回结果
# results = loop.run_until_complete(main())
# for result in results:
#     print('Task 返回结果：',result)

#4种获取返回结果
# dones,pending = loop.run_until_complete(main())
# for task in dones:
#     print('Task 的返回结果：',task.result())

##5.获取返回结果
loop.run_until_complete(main())

print('TIME:',time.time()-start)