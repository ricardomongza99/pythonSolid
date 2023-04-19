from typing import List
from models import Movie
from config import URL, FILE_PATH, FIELDNAMES
from movie_fetchers import MovieFetcher, IMDBMovieFetcher
from movie_writers import MovieWriter, CSVMovieWriter


def main():
    # Can use any MovieFetch in the future (rotten tomatoes, metacritic, etc.)
    movie_fetcher: MovieFetcher = IMDBMovieFetcher(url=URL)
    movies: List[Movie] = movie_fetcher.fetch_movies()

    # Can use any MovieWriter in the future (pdf, txt, md, etc.)
    movie_writer: MovieWriter = CSVMovieWriter(file_path=FILE_PATH, fieldnames=FIELDNAMES)
    movie_writer.write_movies(movies)


if __name__ == '__main__':
    main()
