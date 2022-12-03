import json
from asyncio import StreamReader, StreamWriter

from loguru import logger


async def register(reader: StreamReader, writer: StreamWriter, username: str) -> dict[str, str]:
    data = await reader.readline()
    logger.debug(data.decode())

    writer.write("\n".encode())
    await writer.drain()

    data = await reader.readline()
    logger.debug(data.decode())

    writer.write(f"{username}\n".encode())
    await writer.drain()

    data = await reader.readline()
    logger.debug(data.decode())

    return json.loads(data.decode())
