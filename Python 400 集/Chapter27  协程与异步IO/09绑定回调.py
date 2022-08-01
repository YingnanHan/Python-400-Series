import time,asyncio
async def do_work(x):
    print('waiting:',x)
    return 'Done after {}s'.format(x)
#定义回调函数
def callback(future):
    print('Callback:',future.result())
#获取协程对象
coroutine = do_work(3)
#创建事件循环
loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)
#给任务添加绑定函数
# task.add_done_callback(callback)
loop.run_until_complete(task)
#直接调用task中的result来获取返回结果
print('直接获取返回结果：',task.result())