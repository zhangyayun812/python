# -*- coding: utf-8 -*-
import asyncio 
import aiohttp 

async def fetch():     
    async with aiohttp.ClientSession() as session:         
        async with session.get("http://www.baidu.com") as response:                
            response = await response.read()                         
            print(response) 
  
loop = asyncio.get_event_loop() 
loop.run_until_complete(fetch())
