import datetime


def format_msg(msg: str) -> str:
    now = datetime.datetime.now()

    timestamp = now.strftime("%d/%m/%Y %H:%M")
    return f"[{timestamp}] {msg}"