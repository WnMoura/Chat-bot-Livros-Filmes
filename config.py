import os 


TMDB_API_KEY = os.getenv("TMDB_API_KEY", "90fd4b6b1db3e08080930ee4b02c342a")
GOOGLE_BOOKS_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY", "AIzaSyBmwDJnlq2lWFqtjBLKetL5hT3Bl0tZ0XU")


DATABASE_PATH = "data/chatbot.db"