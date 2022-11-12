import asyncio
import json

from loguru import logger


async def authorise(token: str) -> tuple[asyncio.StreamWriter, dict|None]:
    reader, writer = await asyncio.open_connection("minechat.dvmn.org", 5050)
    data = await reader.readline()
    logger.debug(data.decode())

    writer.write(f"{token}\n".encode())
    await writer.drain()

    data = await reader.readline()
    logger.debug(data.decode())
    return writer, json.loads(data.decode())