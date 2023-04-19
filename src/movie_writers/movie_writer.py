from abc import ABC, abstractmethod
from typing import List
from models import Movie


class MovieWriter(ABC):
    @abstractmethod
    def write_movies(self, movies: List[Movie]):
        pass
