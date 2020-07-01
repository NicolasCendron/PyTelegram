import json
import os
from quart import Quart, request, jsonify

from telethon import TelegramClient
# Substituir
data = []
with open('config.json') as config_file:
    data = json.load(config_file)

api_id = data['api_id']
api_hash = data['api_hash']

app = Quart(__name__)
app.secret_key = data['password']


def acesso_negado():
    return jsonify({"success": False,"message": "Access Denied"}), 403

@app.route('/sendTelegramMessage', methods=['POST'])
async def post_mandaMensagem():
    try:    
        client = TelegramClient('session', api_id, api_hash)
        await client.connect()
    
        dados_requisicao = await request.get_json()

        password = dados_requisicao.get("password", None)
        if password is None or password != app.secret_key:
            return acesso_negado()

        telefone = dados_requisicao.get("phone", None)
        if telefone is None:
            return jsonify({"message": "Phone Not Found."})

        mensagem = dados_requisicao.get("message", None)
        if mensagem is None:
            return jsonify({"message": "Message not found."})

        await client.send_message(telefone, mensagem)
        print("Sent Message to number: " + telefone);
        await client.disconnect()
        return jsonify({"success": True}), 200
    except Exception as e:
        print(e)
        strErro = "";        
        if hasattr(e, 'message'):
            strErro = e.message
        return jsonify({"success": False, "message": str(e),"message2": strErro}), 500
      
if __name__ == "__main__":
    print("Telegram Begin")
    host_config = data["host"]
    port_config = data["port"]
    app.run(host=host_config, port=port_config)

