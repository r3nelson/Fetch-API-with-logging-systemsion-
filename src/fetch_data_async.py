import aiohttp
from log import logger

async def fetch_data_async(url, log_file):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:

                # request successful
                if response.status == 200:
                    logger(log_file).debug(f'"{url}" returned http 200: OK')
                    return await response.text()

                # request URL is wrong on internet is down        
                if response.status == 404:
                    logger(log_file).info(f'Internet error')
                    logger(log_file).debug(f'"{url}" returned http 404: NOT FOUND')
                    logger(log_file).error(f'"{url}" was not found\nSee if URL was misinputted or if it is currently down ')    
                    return                 
                
                # Any other error
                else:
                    logger(log_file).debug(f"{url} returned http status code: {response.status} error")
                    logger(log_file).error(f"Failed to fetch data")
                    return 
                         
    except aiohttp.ClientError as e:
        logger(log_file).error(f"Some other error occured. Please see logs\nError during request: {e}")
        return 
    
