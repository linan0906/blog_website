from www import orm
import asyncio
from www.models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='123456', db='awesome')
    #u = User(name='Test', email='test@qq.com', passwd='1234567890', image='about:blank')
    u = User( id='3',name='test', email='789654321@qq.com', passwd='1234567890', image='about:blue')
    await u.save()
    #添加到数据库后需要关闭连接池，否则可能会报错
    orm.__pool.close()
    await orm.__pool.wait_closed()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()

