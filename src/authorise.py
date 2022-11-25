import json
from asyncio import StreamReader, StreamWriter

from loguru import logger


async def authorise(reader: StreamReader, writer: StreamWriter, token: str) -> bool:
    data = await reader.readline()
    logger.debug(data.decode())

    writer.write(f"{token}\n".encode())
    await writer.drain()

    data = await reader.readline()
    logger.debug(data.decode())

    if not json.loads(data.decode()):
        logger.error("Incorrect token. Authorization failed.")
        return False

    return True