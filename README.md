# Chat Client

A tool to connect to Minecraft chat

## Install Requirements

```sh
pip3 requirements.txt
```

## Reading the chat

```sh
python3 read_chat.py --host minechat.dvmn.org --port 5000 --history minechat.history
```

## Configuration options

| Key     | Description                | Required |
| ------- | -------------------------- | -------- |
| host    | Host of chat to connect to | False    |
| port    | Port of chat to connect to | False    |
| history | File to save chat history  | False    |

## Writing to the chat

```sh
python3 write_chat.py --message "Hello chat" --host minechat.dvmn.org --port 5050 --history minechat.history --username some_username
```

## Configuration options

| Key      | Description                | Required |
| -------- | -------------------------- | -------- |
| message  | Message to send            | True     |
| host     | Host of chat to connect to | False    |
| port     | Port of chat to connect to | False    |
| history  | File to save chat history  | False    |
| token    | Chat access token          | False    |
| username | Nickname for new user      | False    |
