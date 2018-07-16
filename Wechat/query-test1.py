# -*- coding: utf-8 -*-
import aiohttp
import asyncio
import sys, os
import aiofiles
from datetime import datetime 
from time import time
import json

#使用async以及await关键字将函数异步化。在hello()中实际上有两个异步操作：首先异步获取相应，然后异步读取响应的内容。
async def fetch(url, session, sem):
    #conn = aiohttp.TCPConnector(limit=30)
    #async with aiohttp.ClientSession(headers={"Cookie":"JSESSIONID={}".format(jsessionId)}) as session:
    async with sem:
        async with session.get(url) as resp:
            #不加下面这一行的话，不会实现协程异步
            await asyncio.sleep(0)
            return await resp.read()
"""
async def fetch(url, jsessionId, sem):
    async with sem:
        async with aiohttp.ClientSession(headers={"Cookie":"JSESSIONID={}".format(jsessionId)}) as session:
            async with session.get(url) as resp:
                #async print(url)
                await asyncio.sleep(0)
                return await resp.read()
"""

async def run():
    tasks = []
    numbers = []
    url = "http://211.137.107.18:8888/cm/user!queryMonthInfoByMsisdn.action?msisdn={}&serviceType=B"
    jsessionId = 'A3FB6AA9CE57ACB5CF105E9428CE0AB2'
    #脚本名：sys.argv[0],参数1：sys.argv[1],参数2：sys.argv[2]
    file = sys.argv[1]
    #会报：concurrent.futures._base.TimeoutError原因为：Once it's a big number such as 30,000 it can't be physically done within 10 seconds due to networks/ram/cpu capacity.所以需要限制携程的信号量
    sem = asyncio.Semaphore(1000)
    #将session以参数传入fetch中，让所有请求只使用一个session，而不用每个请求都创建一个session
    async with aiohttp.ClientSession(headers={"Cookie":"JSESSIONID={}".format(jsessionId)}) as session:
        if os.path.isfile(file):
            with open(file, mode = 'r') as f:
                for line in f:
                    #split()默认以空格分隔
                    phoneNumber = line.split()[0]
                    numbers.append(phoneNumber)
                    #print(url.format(phoneNumber))
                    #task = asyncio.ensure_future(fetch(url.format(phoneNumber), jssessionId))
                    task = fetch(url.format(phoneNumber), session, sem)
                    tasks.append(task)
            	##它搜集所有的Future对象，然后等待他们返回
            
            responses = await asyncio.gather(*tasks)
            for j in range(len(responses)):
                resJson = json.loads(responses[j].decode('utf-8'))
                if resJson["reDesc"] != "[FCMG]操作成功":
                    print('{}:{}'.format(numbers[j],responses[j].decode('utf-8')))
        else:
            print("{} not found".format(file))

a = datetime.now()
#a = time()
#创建一个asyncio loop的实例， 然后将任务加入其中
loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.close()
b = datetime.now()
#b = time()
print("{}:{}".format(a, b))
print('Cost {} seconds'.format((b - a).seconds))
