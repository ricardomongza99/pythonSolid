# Single Responsibility Principle (SRP): The Movie class only handles storing movie information.
class Movie:
    def __init__(self, movie_title: str, year: str, place: str, star_cast: str, rating: str, vote: str, link: str, preference_key: int):
        self.movie_title = movie_title
        self.year = year
        self.place = place
        self.star_cast = star_cast
        self.rating = rating
        self.vote = vote
        self.link = link
        self.preference_key = preference_key
