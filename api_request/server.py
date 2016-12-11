from flask import Flask, render_template

from call-api import call_api


app = Flask(__name__)


@app.route("/details")
def display_details():
	"""call helper function to get details on 1 movie"""

	call_api()


    return render_template('details.html',
    						title=title,
    						poster=poster,
    						synopsis=synopsis,
    						ave_rating=ave_rating,
    						)



if __name__ == "__main__":
    app.run(host="0.0.0.0")