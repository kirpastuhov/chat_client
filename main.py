import asyncio
import datetime

import aiofiles
from loguru import logger


async def tcp_echo_client(message):
    host = "minechat.dvmn.org"
    port = 5000
    reader, writer = await asyncio.open_connection(host, port)

    async with aiofiles.open('msg_log.txt', mode='a') as log_file:
        while not reader.at_eof():
            data = await reader.readline()
            message = format_msg(data.decode())

            print(message)
            await log_file.write(message)

    logger.info("Close the connection")
    writer.close()


def format_msg(msg):
    now = datetime.datetime.now()

    timestamp = now.strftime("%d/%m/%Y %H:%M")
    return f"[{timestamp}] {msg}"

if __name__ == "__main__":
    asyncio.run(tcp_echo_client("Hello World!"))

