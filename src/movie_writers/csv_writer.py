import csv
from typing import List
from models import Movie
from . import MovieWriter


# Interface Segregation Principle (ISP) and Liskov Substitution Principle (LSP): The MovieWriter abstract base class
# defines a common interface for writing movies.
class CSVMovieWriter(MovieWriter):
    def __init__(self, file_path: str, fieldnames: List[str]):
        self.file_path = file_path
        self.fieldnames = fieldnames

    def write_movies(self, movies: List[Movie]):
        with open(self.file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for movie in movies:
                writer.writerow(movie.__dict__)