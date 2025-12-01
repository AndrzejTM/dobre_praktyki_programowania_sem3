from fastapi import FastAPI
from typing import List
from database import SessionLocal
from models import Movie, Link, Rating, Tag

app = FastAPI(title="Movies Database API (SQLite)")


# ░░░░░░░░░░░░░░░░
#  Helpery
# ░░░░░░░░░░░░░░░░

def serialize(obj):
    """Konwertuje obiekt SQLAlchemy na dict"""
    data = {}
    for column in obj.__table__.columns:
        data[column.name] = getattr(obj, column.name)
    return data


def serialize_list(objects):
    return [serialize(o) for o in objects]


# ░░░░░░░░░░
#  Endpointy
# ░░░░░░░░░░

@app.get("/")
def read_root():
    return {"hello": "world"}


# FILMY --------------------------------------------------------------------------

@app.get("/movies")
def get_movies():
    session = SessionLocal()
    movies = session.query(Movie).all()
    session.close()
    return serialize_list(movies)


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    session = SessionLocal()
    movie = session.query(Movie).filter(Movie.movieId == movie_id).first()
    session.close()

    if not movie:
        return {"error": "Movie not found"}

    return serialize(movie)


# LINKI --------------------------------------------------------------------------

@app.get("/links")
def get_links():
    session = SessionLocal()
    links = session.query(Link).all()
    session.close()
    return serialize_list(links)


# OCENY --------------------------------------------------------------------------

@app.get("/ratings")
def get_ratings():
    session = SessionLocal()
    ratings = session.query(Rating).all()
    session.close()
    return serialize_list(ratings)


@app.get("/ratings/movie/{movie_id}")
def get_ratings_for_movie(movie_id: int):
    session = SessionLocal()
    ratings = session.query(Rating).filter(Rating.movieId == movie_id).all()
    session.close()
    return serialize_list(ratings)


# TAGI ---------------------------------------------------------------------------

@app.get("/tags")
def get_tags():
    session = SessionLocal()
    tags = session.query(Tag).all()
    session.close()
    return serialize_list(tags)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
