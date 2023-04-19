from abc import ABC, abstractmethod
from typing import List
from models import Movie


# Interface Segregation Principle (ISP) and Liskov Substitution Principle (LSP): The MovieFetcher
# abstract base class defines a common interface for fetching movies.
class MovieFetcher(ABC):
    @abstractmethod
    def fetch_movies(self) -> List[Movie]:
        pass
