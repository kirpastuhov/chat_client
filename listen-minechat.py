import argparse
import asyncio
import datetime

import aiofiles
from loguru import logger


async def listen(message):
    parser = argparse.ArgumentParser(description="Client settings")
    parser.add_argument("--host", dest="host", type=str, default="minechat.dvmn.og", help="Host to listen")
    parser.add_argument("--port", dest="port", type=str, default="5005", help="Port")
    parser.add_argument("--history", dest="history_path", type=str, default="minechat.history", help="File for message history.")
    args = parser.parse_args()


    reader, writer = await asyncio.open_connection(args.host, args.port)

    async with aiofiles.open(args.history_path, mode='a') as log_file:
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
    asyncio.run(listen("Hello World!"))

