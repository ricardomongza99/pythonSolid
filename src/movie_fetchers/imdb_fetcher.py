import requests
import re
from bs4 import BeautifulSoup
from typing import List
from models import Movie
from . import MovieFetcher


class IMDBMovieFetcher(MovieFetcher):
    def __init__(self, url):
        self.url = url


    def fetch_movies(self) -> List[Movie]:
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'lxml')

        movies = soup.select('td.titleColumn')
        links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
        crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
        ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
        votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

        movie_list = []

        for index in range(0, len(movies)):
            movie_string = movies[index].get_text()
            movie = (' '.join(movie_string.split()).replace('.', ''))
            movie_title = movie[len(str(index)) + 1:-7]
            year = re.search('\((.*?)\)', movie_string).group(1)
            place = movie[:len(str(index)) - (len(movie))]

            data = Movie(movie_title=movie_title,
                         year=year,
                         place=place,
                         star_cast=crew[index],
                         rating=ratings[index],
                         vote=votes[index],
                         link=links[index],
                         preference_key=index % 4 + 1)
            movie_list.append(data)

        return movie_list
