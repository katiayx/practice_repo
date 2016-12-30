import os

import requests

EB_TOKEN = os.environ["EB_TOKEN"]
payload = {"q": "python", "sort_by": "date", "start_date.keyword": "next_week"}
search_url = "https://www.eventbriteapi.com/v3/events/search/"
headers = {'Authorization':'Bearer %s' % EB_TOKEN}

def call_api():
	"""try eventbrite api"""

	response = requests.get(search_url,params=payload,headers=headers)

	r_dict = response.json()

	print r_dict

call_api()
