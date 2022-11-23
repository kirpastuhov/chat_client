from asyncio.streams import StreamReader

import aiofiles
from loguru import logger

from src.utils import format_msg


async def listen(reader: StreamReader, history_path: str):
    async with aiofiles.open(history_path, mode='a') as log_file:
        while not reader.at_eof():
            data = await reader.readline()
            message = format_msg(data.decode())
            await log_file.write(message)
            logger.debug(message)
