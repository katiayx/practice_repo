import os

import requests

EB_TOKEN = os.environ["EB_TOKEN"]
MEETUP_TOKEN = os.environ["MEETUP_TOKEN"]


def search_eventbrite():
	""" """

	payload = {"q": "python", "sort_by": "date", "start_date.keyword": "next_week"}
	search_url = "https://www.eventbriteapi.com/v3/events/search/"
	headers = {'Authorization':'Bearer %s' % EB_TOKEN}

	response = requests.get(search_url,params=payload,headers=headers)

	r_dict = response.json()

	print r_dict

call_api()


def search_meetup():
	""" """

	payload = {"q": "python", "sort_by": "date", "start_date.keyword": "next_week"}
	search_url = "https://www.eventbriteapi.com/v3/events/search/"
	headers = {'Authorization':'Bearer %s' % EB_TOKEN}
