from abc import ABC, abstractmethod
from typing import List
from models import Movie


class MovieFetcher(ABC):
    @abstractmethod
    def fetch_movies(self) -> List[Movie]:
        pass
