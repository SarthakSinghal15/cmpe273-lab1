import asyncio
import requests

async def main():
    url ='https://webhook.site/b361e66d-cbfe-485d-bc88-790946eaf5e7'
    tasks = []
    for i in range(3):
        tasks.append(loop.run_in_executor(None,requests.get,url))
    for response in await asyncio.gather(*tasks):
        print(response.headers['Date'])  

loop = asyncio.get_event_loop()
loop.run_until_complete(main())