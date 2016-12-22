import os

import requests

evtbrite_api = os.environ["evtbrite_api"]


payload = {"q": "python", "sort_by": "date", "start_date.keyword": "next_week"}
evtburl = "https://www.eventbriteapi.com/v3/events/search/&token=" + evtbrite_api

def call_api():
	"""try eventbrite api"""

	response = requests.get(evtburl, params=payload)
	r_dict = response.json()

	print r_dict

call_api()
