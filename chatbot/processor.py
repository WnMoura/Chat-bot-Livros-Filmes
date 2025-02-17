import nltk
from nltk.tokenize import RegexpTokenizer

nltk.download("punkt")

def processar_mensagem(mensagem):
    tokenizer = RegexpTokenizer(r"\w+")  # Tokeniza apenas palavras (evita erros)
    palavras = tokenizer.tokenize(mensagem.lower())
    print("Tokens:", palavras)  # Para depuração
    return "Filme" if "filme" in palavras else "Livro" if "livro" in palavras else None
