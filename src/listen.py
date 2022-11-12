import asyncio

import aiofiles
from loguru import logger

from src.utils import format_msg


async def listen(host: str, port: int, history_path: str):
    logger.info(f"Connecting to {host}:{port}")
    reader, writer = await asyncio.open_connection(host, port)

    async with aiofiles.open(history_path, mode='a') as log_file:
        while not reader.at_eof():
            data = await reader.readline()
            message = format_msg(data.decode())
            await log_file.write(message)
            logger.debug(message)

    logger.debug("Close the connection")
    writer.close()

