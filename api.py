from fastapi import FastAPI
from typing import List, Optional
import csv
from pathlib import Path

app = FastAPI(title="Movies Database API")


# Modele danych
class Movie:
    def __init__(self, movieId: str, title: str, genres: str):
        self.movieId = int(movieId)
        self.title = title
        self.genres = genres.split('|') if genres else []


class Link:
    def __init__(self, movieId: str, imdbId: str, tmdbId: str):
        self.movieId = int(movieId)
        self.imdbId = imdbId
        self.tmdbId = tmdbId if tmdbId else None


class Rating:
    def __init__(self, userId: str, movieId: str, rating: str, timestamp: str):
        self.userId = int(userId)
        self.movieId = int(movieId)
        self.rating = float(rating)
        self.timestamp = int(timestamp)


class Tag:
    def __init__(self, userId: str, movieId: str, tag: str, timestamp: str):
        self.userId = int(userId)
        self.movieId = int(movieId)
        self.tag = tag
        self.timestamp = int(timestamp)


# Funkcje pomocnicze do wczytywania danych
def load_csv(filename: str, skip_header: bool = True):
    """Wczytuje dane z pliku CSV"""
    filepath = Path(filename)
    if not filepath.exists():
        return []

    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        if skip_header:
            next(reader)  # Pomiń nagłówek
        return list(reader)


def serialize_objects(objects: List) -> List[dict]:
    """Serializuje listę obiektów do listy słowników"""
    return [obj.__dict__ for obj in objects]


# Endpointy API
@app.get("/")
def read_root():
    """Podstawowy endpoint powitalny"""
    return {"hello": "world"}


@app.get("/movies")
def get_movies():
    """Zwraca listę wszystkich filmów"""
    rows = load_csv("movies.csv")
    movies = []

    for row in rows:
        if len(row) >= 3:
            movie = Movie(row[0], row[1], row[2])
            movies.append(movie)

    return serialize_objects(movies)


@app.get("/links")
def get_links():
    """Zwraca listę linków do filmów (IMDB, TMDB)"""
    rows = load_csv("links.csv")
    links = []

    for row in rows:
        if len(row) >= 3:
            link = Link(row[0], row[1], row[2] if len(row) > 2 else "")
            links.append(link)

    return serialize_objects(links)


@app.get("/ratings")
def get_ratings():
    """Zwraca listę ocen filmów"""
    rows = load_csv("ratings.csv")
    ratings = []

    for row in rows:
        if len(row) >= 4:
            rating = Rating(row[0], row[1], row[2], row[3])
            ratings.append(rating)

    return serialize_objects(ratings)


@app.get("/tags")
def get_tags():
    """Zwraca listę tagów filmów"""
    rows = load_csv("tags.csv")
    tags = []

    for row in rows:
        if len(row) >= 4:
            tag = Tag(row[0], row[1], row[2], row[3])
            tags.append(tag)

    return serialize_objects(tags)


# Dodatkowe endpointy z filtrowaniem
@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    """Zwraca konkretny film po ID"""
    rows = load_csv("movies.csv")

    for row in rows:
        if len(row) >= 3 and int(row[0]) == movie_id:
            movie = Movie(row[0], row[1], row[2])
            return movie.__dict__

    return {"error": "Movie not found"}


@app.get("/ratings/movie/{movie_id}")
def get_ratings_for_movie(movie_id: int):
    """Zwraca oceny dla konkretnego filmu"""
    rows = load_csv("ratings.csv")
    ratings = []

    for row in rows:
        if len(row) >= 4 and int(row[1]) == movie_id:
            rating = Rating(row[0], row[1], row[2], row[3])
            ratings.append(rating)

    return serialize_objects(ratings)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)