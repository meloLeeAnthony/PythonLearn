import asyncio


async def do_work(x):
    print('waiting:', x)
    return 'Done after {}s'.format(x)


# 定义回调函数
def callback(future):
    print('Callback:', future.result())


# 获取协程对象
coroutine = do_work(3)
# 1、创建事件循环
loop = asyncio.get_event_loop()
# 2、创建task对象
task = loop.create_task(coroutine)
# 3、给任务添加绑定函数
task.add_done_callback(callback)
# 4.将协程对象加入到事件循环中
loop.run_until_complete(task)
# 也可以直接调用task中的result来获取返回结果
print('直接获取返回结果：', task.result())
