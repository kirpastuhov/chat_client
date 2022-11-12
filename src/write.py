import asyncio


async def submit_message(message: str, writer: asyncio.StreamWriter):
    writer.write(f"{message}\n\n".encode())
    await writer.drain()

    writer.close()