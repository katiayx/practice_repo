from flask import (Flask, render_template, redirect, request, jsonify)

from jinja2 import StrictUndefined

app = Flask(__name__)

@app.route('/')
def display_search():
    """display search page."""

    return render_template('search.html')

@app.route('/', methods=['POST'])
def get_user_inputs():
    """grab user inputs"""

    params = {}
    params["q"] = request.form.get("q")
    params["sort_by"] = request.form.get("sort_by")
    params["location.address"] = request.form.get("location.address")
    params["location.within"] = request.form.get("location.within")
    params["price"] = request.form.get("price")
    params["start_date.range_start"] = request.form.get("start_date.range_start")
    params["start_date.range_end"] = request.form.get("start_date.range_end")
    params["start_date.keyword"] = request.form.get("start_date.keyword")


    return render_template('results.html',
                        )



if __name__ == "__main__":
    app.run(host="0.0.0.0")
