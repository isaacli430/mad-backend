import aiohttp, asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post("http://165.227.53.150:8000/post?message=heythere") as resp:
            data = await resp.json()
            print(data)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())