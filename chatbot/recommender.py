import requests
from config import TMDB_API_KEY, GOOGLE_BOOKS_API_KEY


def recomendar_filme():
    url =  f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=pt-BR"
    response = requests.get(url)


    if response.status_code == 200:
        filmes = response.json()["results"]
        return [f"{filme['title']} - {filme['overview']}" for filme in filmes[:5]]
    return ["Erro ao buscar filmes."]

def recomendar_livro():
    url = f"https://www.googleapis.com/books/v1/volumes?q=best&key={GOOGLE_BOOKS_API_KEY}"
    response = requests.get(url)


    if response.status_code == 200:
        livros = response.json()["items"]
        return [f"📖 {livro['volumeInfo']['title']} - {livro['volumeInfo'].get('authors', ['Autor desconhecido'])[0]}" for livro in livros[:5]]
    return ["Erro ao buscar livros."]
