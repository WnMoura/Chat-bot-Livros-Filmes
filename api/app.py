from flask import Flask, request, jsonify
from chatbot.bot import responder_usuario

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    dados = request.json
    mensagem = dados.get("mensagem", "")
    resposta = responder_usuario(mensagem)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)