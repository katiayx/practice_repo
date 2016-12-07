import os

import requests

movie_db_api = os.environ["movie_db_api"]

MOVIEDB = "https://api.themoviedb.org/3/discover/movie?api_key=" + movie_db_api + "&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&primary_release_date.gte=2016-12-04&primary_release_date.lte=2016-12-06&with_release_type=3%7C2&with_original_language=en"


response = requests.get(MOVIEDB)
r_dict = response.json()

for i in r_dict['results']:
    movie_name = i.get('title')
    print movie_name
