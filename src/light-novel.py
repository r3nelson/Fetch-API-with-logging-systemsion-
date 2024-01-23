import os
import asyncio
from fetch_data_async import fetch_data_async
from log import logger

async def main():
    # set URL to be link to data source
    url = "http://localhost:4000/light-novel" 

    # get name of file executing code without extension
    file_name = os.path.basename(__file__)
    file_name = os.path.splitext(file_name)[0]
     
    # fetch data and log data to path "./logs/<filename>/<file_name>.log"
    data = await fetch_data_async(url, file_name)

    # test unique case where data isn't empty but is string of an empty value
    if data == '{}' or data == '[]' or data == '()':
        logger(file_name).debug(f'fetch request to {url} returned:\n\tdata: {data}\n\ttype: {type(data)}')
        logger(file_name).info(f'{url} has no data')
        return logger(file_name).error('No data was returned from fetch')
    # if there is some truthy value for data
    elif data: 
        return logger(file_name).info(f"data fetched succesfully")
    # if data is any other falsey value
    else: 
        logger(file_name).debug(f'fetch request to {url} returned:\n\tdata: {data}\n\ttype: {type(data)}')
        logger(file_name).info(f'{url} has no data')
        return logger(file_name).error('No data was returned from fetch')      

# Run the event loop
asyncio.run(main())