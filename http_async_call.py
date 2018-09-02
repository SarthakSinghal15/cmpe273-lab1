import asyncio
import requests
import aiohttp

async def main():
    url ='https://webhook.site/b361e66d-cbfe-485d-bc88-790946eaf5e7'
    tasks = []
    for i in range(3):
        tasks.append(task.run_in_executor(None,requests.get,url))
    for response in await asyncio.gather(*tasks):
        print(response.headers['Date'])
        
    #Using aiohttp(Uncomment the below lines and comment the above code in main----

    #async with aiohttp.ClientSession() as ClientSession:
        #futures = [get_url(ClientSession,url) for i in range(3)]
        #for response in await asyncio.gather(*futures):
            #print(response.headers['Date'])            

#async def get_url(session,url):
    #async with session.head(url) as response:
        #return response


task = asyncio.get_event_loop()
task.run_until_complete(main())