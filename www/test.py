import asyncio
import easy_orm
from models import User, Blog, Comment


async def test(loop,**kw):
    await easy_orm.create_pool(loop=loop, host='127.0.0.1', port=3306,user='www-data', password='www-data', db='awesome')

    u = User(name=kw.get('name'), email=kw.get('email'), passwd=kw.get('passwd'), image=kw.get('image'))
    await u.save()
    await easy_orm.destory_pool()

data=dict(name='gafff', email='225123345@qq.com', passwd='1312345', image='about:blank')
# 获取EventLoop:
loop = asyncio.get_event_loop()

#把协程丢到EventLoop中执行
loop.run_until_complete(test(loop,**data))

#关闭EventLoop
loop.close()