import json
import os
from quart import Quart, request, jsonify
import asyncio
from telethon import TelegramClient
# Substituir
data = []
with open('config.json') as config_file:
    data = json.load(config_file)

api_id = data['api_id']
api_hash = data['api_hash']

app = Quart(__name__)
app.secret_key = data['password']

async def setup():
    try:
        client = TelegramClient('session', api_id, api_hash)
        print("************* BEGIN CONFIG *************")
        await client.start()
        print("************* CONFIG SUCCESS *************")
        print("************* SESSION FILE GENERATED  *************")
        await client.disconnect()
        print("************* SESSION FILE GENERATED  *************")
    except:
        print(e)
        strErro = "";
        if hasattr(e, 'message'):
            print(e.message)

async def main():
    await setup()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
