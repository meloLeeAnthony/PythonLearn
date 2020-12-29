import asyncio
import time


async def do_work(x):
    print('waitting:', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


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

start = time.time()
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(asyncio.wait(tasks))


except KeyboardInterrupt as e:
    '''
        按ctrl + c以后发生的事件
        {
            <Task finished coro=<do_work() done, defined at ./21-Coroutine纤程/13协程停止.py:5> result='Done after 2s'>, 
            <Task pending coro=<wait() running at D:\Python37-32\lib\asyncio\tasks.py:363> wait_for=<Future pending cb=[<TaskWakeupMethWrapper 05-object面向对象 at 0x031B77F0>()]>>, 
            <Task finished coro=<do_work() done, defined at ./21-Coroutine纤程/13协程停止.py:5> result='Done after 1s'>, 
            <Task pending coro=<do_work() running at ./21-Coroutine纤程/13协程停止.py:7> wait_for=<Future pending cb=[<TaskWakeupMethWrapper 05-object面向对象 at 0x031B7770>()]> cb=[_wait.<locals>._on_completion() at D:\Python37-32\lib\asyncio\tasks.py:440]>
        }
    '''
    # 获取事件循环中所有任务列表
    print(asyncio.Task.all_tasks())
    for task in asyncio.Task.all_tasks():
        print(task.cancel())  # 如果返回的True代表当前任务取消成功
    loop.stop()
    loop.run_forever()
finally:
    loop.close()
print('TIME:', time.time() - start)
