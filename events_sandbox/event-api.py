import os

import requests

EB_TOKEN = os.environ["EB_TOKEN"]
payload = {"q": "python", "sort_by": "date", "start_date.keyword": "next_week"}
search_url = "https://www.eventbriteapi.com/v3/events/search/"

def call_api():
	"""try eventbrite api"""

	response = requests.get(search_url,params=payload,
		headers = {"Authorization": "Bearer" + EB_TOKEN},
		verify = True,
	)

	r_dict = response.json()

	print r_dict

call_api()
