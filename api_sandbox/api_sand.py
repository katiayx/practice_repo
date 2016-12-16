import os

import requests

movie_db_api = os.environ["movie_db_api"]

MOVIEDB = "https://api.themoviedb.org/3/movie/550?api_key=" + movie_db_api

def call_api():
	"""get details for 1 movie"""

	response = requests.get(MOVIEDB)
	r_dict = response.json()

	movie_details = {}
	movie_details['title'] = r_dict['original_title']
	movie_details['poster'] = r_dict['poster_path']
	movie_details['synopsis'] = r_dict['overview']
	movie_details['ave_rating'] = r_dict['vote_average']

	return movie_details
