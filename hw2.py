import aiohttp
import asyncio
import os
import random
async def download_random_image(session, url, img):
    async with session.get(url) as response:
        response.raise_for_status()
        file_name = os.path.join(img, f'image_{random.randint(1, 10)}.jpg')
        with open(file_name, 'wb') as file:
            file.write(await response.read())
        print(f"Изображение сохранено как {file_name}")

async def main():
    img = 'images'
    os.makedirs(img, exist_ok=True)
    url = 'https://wallpapers.com/nature#google_vignette'

    async with aiohttp.ClientSession() as session:
        tasks = [download_random_image(session, url, img) for _ in range(10)]
        await asyncio.gather(*tasks)

asyncio.run(main())
