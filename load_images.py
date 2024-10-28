import asyncio
import aiohttp
import load_xl
import config

async def download_file(session, proxy: str | None, filename: str, urls: list):
    file_num = 1
    load_dir = 'feed'
    for url in urls:
        file_suffix = url[-3:]
        full_file_name = f'{load_dir}/{filename}_{file_num}.{file_suffix}'
        if not proxy:
            async with session.get(url) as response:
                await load_images(response, full_file_name)
                
        else:
            async with session.get(url, proxy=proxy) as response:
                await load_images(response, full_file_name)
        file_num +=1
                
                
async def load_images(response, full_file_name):
    
    with open(full_file_name, 'wb') as f:
        while True:
            chunk = await response.content.read(1024)
            if not chunk:
                break
            f.write(chunk)
    print(f"Downloaded {full_file_name}")

                
async def main(xlsx_file_path: str, proxy_str: str | None):
    
    data_for_load: dict = load_xl.get_data_for_load(xlsx_file_path)

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(download_file(session, proxy_str, file_name, url_list)) for file_name, url_list in data_for_load.items()]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    # 'http://{USERNAME}:{PASSWORD}@{PROXY_ADDRESS}'
    asyncio.run(main('sours.xlsx', config.PROXY))
    # import os
    # for item in os.environ.items():
    #     print(item)
