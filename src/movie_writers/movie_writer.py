from abc import ABC, abstractmethod
from typing import List
from models import Movie


# Open/Closed Principle (OCP) and Dependency Inversion Principle (DIP): The CSVMovieWriter class implements the
# MovieWriter interface and can be easily extended or replaced without modifying the rest of the code.
class MovieWriter(ABC):
    @abstractmethod
    def write_movies(self, movies: List[Movie]):
        pass
