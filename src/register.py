import asyncio
import json

from loguru import logger


async def register(host: str, username: str) -> dict[str, str]:
    reader, writer = await asyncio.open_connection(host, 5050)

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

    writer.close()
    return json.loads(data.decode())
