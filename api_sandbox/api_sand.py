import os

import requests

movie_db_api = os.environ["movie_db_api"]

MOVIEDB = "https://api.themoviedb.org/3/movie/550?api_key=" + movie_db_api


def call_api():
	"""get details for 1 movie"""

	response = requests.get(MOVIEDB)
	r_dict = response.json()
	
	title = r_dict['original_title']
	poster = r_dict['poster_path']
	synopsis = r_dict['overview']
	ave_rating = r_dict['vote_average']

	return title, poster, synopsis, ave_rating


