import os

import requests

evtbrite_api = os.environ["evtbrite_api"]


param = {"q": "search", "sort_by": " ", }
MOVIEDB = "www.eventbriteapi.com/v3/events/search/?q=python+&sort_by=date&location.address=San+Francisco&location.within=20mi&price=free&start_date.range_start=2016-12-01&start_date.range_end=2016-12-23&start_date.keyword=this_week&token=" + evtbrite_api

def call_api():
	"""get details for 1 movie"""

	response = requests.get(MOVIEDB, params=payload)
	r_dict = response.json()

	return movie_details
