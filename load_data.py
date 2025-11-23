import pandas as pd
from database import SessionLocal, init_db
from models import Movie, Rating, Tag, Link


def load_movies(session):
    df = pd.read_csv("movies.csv")
    movies = [
        Movie(
            movieId=row.movieId,
            title=row.title,
            genres=row.genres
        )
        for _, row in df.iterrows()
    ]
    session.bulk_save_objects(movies)
    session.commit()


def load_ratings(session):
    df = pd.read_csv("ratings.csv")
    ratings = [
        Rating(
            userId=row.userId,
            movieId=row.movieId,
            rating=row.rating,
            timestamp=row.timestamp
        )
        for _, row in df.iterrows()
    ]
    session.bulk_save_objects(ratings)
    session.commit()


def load_tags(session):
    df = pd.read_csv("tags.csv")
    tags = [
        Tag(
            userId=row.userId,
            movieId=row.movieId,
            tag=row.tag,
            timestamp=row.timestamp
        )
        for _, row in df.iterrows()
    ]
    session.bulk_save_objects(tags)
    session.commit()


def load_links(session):
    df = pd.read_csv("links.csv", dtype=str)
    links = [
        Link(
            movieId=row.movieId,
            imdbId=row.imdbId,
            tmdbId=row.tmdbId
        )
        for _, row in df.iterrows()
    ]
    session.bulk_save_objects(links)
    session.commit()


if __name__ == "__main__":
    init_db()
    db = SessionLocal()

    load_movies(db)
    load_links(db)
    load_ratings(db)
    load_tags(db)

    print("Dane załadowane do bazy SQLite.")
