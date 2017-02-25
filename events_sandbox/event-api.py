import os

import requests

EB_TOKEN = os.environ["EB_TOKEN"]
MEETUP_TOKEN = os.environ["MEETUP_TOKEN"]


def search_eventbrite():
	""" """

	payload = {"q": "python", "sort_by": "date", "start_date.keyword": "next_week"}
	search_url = "https://www.eventbriteapi.com/v3/events/search/"
	headers = {'Authorization':'Bearer %s' % EB_TOKEN}


	response = requests.get(search_url,params=payload,headers=headers).json

	for i in response[key]:


# Example 1 - add to database
# def load_coursera_partners():
#     """Load partners from Coursera API responses into database"""

#     partner_api_response = requests.get(COURSERA_PARTNERS_URL)

#     partner_api_response = partner_api_response.json()

#     partners = partner_api_response['elements']

#     for partner in partners:
#         partner_id = partner.get('id', '<unknown>')
#         name = partner.get('name', '<unknown>')

#         partner = Partner(partner_id=partner_id, name=name)

#         db.session.add(partner)

#     db.session.commit()


#Example 2:
# def search_etsy(keywords, min_price, max_price):
# 	"""Search Etsy shops for listings within a price range.
# 	Each listing is represented by a dictionary. The keys in the dictionary correspond with 
# 	the listing id, listing origin, title, price, description, URL, and image URLs of the listing.
# 	Returns number of listings and a list of dictionaries.
# 	"""

# 	etsy_shop_ids = [7877556, 10879226, 7777338, 10537127, 8543678, 10879226, 7023347, 6951911]
# 	etsy_listings = []
# 	count = 0
# 	exclude = ["jewelry", "bead", "ring", "bracelet", "necklace", "earrings"]

# 	for shop_id in etsy_shop_ids:
# 		etsy_parameters = {
# 			"api_key": etsy_api_key,
# 			"shop_id_or_name": shop_id,
# 			"keywords": keywords,
# 			"min_price": float(min_price),
# 			"max_price": float(max_price),
# 			"limit": 100,
# 		}

# 		r = requests.get("https://openapi.etsy.com/v2/shops/%s/listings/active" % shop_id, params=etsy_parameters).json()

# 		for listing in r["results"]:
# 			if not any(word in listing["title"] for word in exclude):
# 				images = requests.get("https://openapi.etsy.com/v2/listings/" + str(listing["listing_id"]) + "/images?api_key=" + etsy_api_key).json()
# 				image_urls = [image["url_fullxfull"] for image in images["results"]]
				
# 				etsy_listings.append(
# 					{
# 					"listing_id": listing["listing_id"],
# 					"listing_origin": "etsy",
# 					"title": listing["title"],
# 					"price": listing["price"], 
# 					"description": listing["description"],
# 					"url": listing["url"],
# 					"image_urls": image_urls
# 					}
# 				)

# 				count += 1

# 	return count, etsy_listings


	




call_api()


def search_meetup():
	""" """

	payload = {"q": "python", "sort_by": "date", "start_date.keyword": "next_week"}
	search_url = "https://www.eventbriteapi.com/v3/events/search/"
	headers = {'Authorization':'Bearer %s' % EB_TOKEN}




