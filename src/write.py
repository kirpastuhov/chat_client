from asyncio import StreamWriter


async def submit_message(message: str, writer: StreamWriter):
    writer.write(f"{message}\n\n".encode())
    await writer.drain()