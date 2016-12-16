from flask import (Flask, render_template, redirect, request, jsonify)

from jinja2 import StrictUndefined

from api_sand import call_api


app = Flask(__name__)

@app.route("/")
def display_details():
	"""call helper function to get details on 1 movie"""

	movie_details = call_api()

	title = movie_details['title']
	poster = movie_details['poster']
	synopsis = movie_details['synopsis']
	ave_rating = movie_details['ave_rating']


	return render_template('details.html',
							title=title,
							poster=poster,
							synopsis=synopsis,
							ave_rating=ave_rating,
							)



if __name__ == "__main__":
    app.run(host="0.0.0.0")
