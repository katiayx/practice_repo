import os

import requests
import json
from pprint import pprint

movie_db_api = os.environment["movie_db_api"]

MOVIEDB = "https://api.themoviedb.org/3/discover/movie?api_key=movie_db_api&sort_by=popularity.desc&vote_average.gte=3&vote_average.lte=5"


def get_api_results():

    response = requests.get(MOVIEDB)
    response = response.json()

    movies = response['results']

    for movie in movies:
        movie_id = movie.get('id')
        movie_name = movie.get('title')

    print movie_id, movie_name


get_api_results()


