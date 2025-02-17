from chatbot.bot import responder_usuario

print("Chatbot de Recomendações - Digite 'sair' para encerrar.")

while True:
    mensagem = input("Voce: ")
    if mensagem.lower() == "sair":
        break
    resposta = responder_usuario(mensagem)
    for r in resposta:
        print(f"Bot: {r}")