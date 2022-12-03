import argparse
import asyncio

from loguru import logger

from src.authorise import authorise
from src.chat_connector import open_connection
from src.register import register
from src.write import submit_message


async def main():
    parser = argparse.ArgumentParser(description="Client settings")
    parser.add_argument("--message", dest="message", type=str, required=True, help="Message to write")
    parser.add_argument("--host", dest="host", type=str, default="minechat.dvmn.org", help="Host to listen")
    parser.add_argument("--port", dest="port", type=str, default="5050", help="Port")
    parser.add_argument("--token", dest="token", type=str, help="Chat access token")
    parser.add_argument("--username", dest="username", type=str, help="Chat username")
    parser.add_argument("--history", dest="history_path", type=str, default="minechat.history", help="File for message history.")
    args = parser.parse_args()

    if not args.token:
        try:
            async with open_connection(args.host, args.port) as conn:
                reader, writer = conn
                response = await register(reader, writer, args.username)
                args.token = response["account_hash"]
        except RuntimeError:
            logger.error("Exiting...")
            quit()

    try:
        async with open_connection(args.host, args.port) as conn:
            reader, writer = conn

            if not await authorise(reader, writer, args.token):
                quit()

            logger.info("Authorization was successful")

            await submit_message(args.message, writer)
            logger.info("Message was sent")

    except RuntimeError:
        logger.error("Exiting...")
        quit()


if __name__ == "__main__":
    asyncio.run(main())
