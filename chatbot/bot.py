from chatbot.processor import processar_mensagem
from chatbot.recommender import recomendar_filme, recomendar_livro

def responder_usuario(mensagem):
    tipo = processar_mensagem(mensagem)

    
    if tipo == "Filme":
        return recomendar_filme()
    elif tipo == "Livro":
        return recomendar_livro()
    else:
        return["Não entendi. Você quer um filme ou um livro?"]