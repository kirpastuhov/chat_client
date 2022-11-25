import argparse
import asyncio

from loguru import logger

from src.chat_connector import open_connection
from src.listen import listen


async def main():
    parser = argparse.ArgumentParser(description="Client settings")
    parser.add_argument("--host", dest="host", type=str, default="minechat.dvmn.org", help="Host to listen")
    parser.add_argument("--port", dest="port", type=str, default="5000", help="Port")
    parser.add_argument("--history", dest="history_path", type=str, default="minechat.history", help="File for message history.")
    args = parser.parse_args()

    try:
        async with open_connection(args.host, args.port) as conn:
            reader, _ = conn
            await listen(reader, args.history_path)
    except RuntimeError:
        logger.error("Exiting...")
        quit()



if __name__ == "__main__":
    asyncio.run(main())
