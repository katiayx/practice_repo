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

    q = request.form.get



if __name__ == "__main__":
    app.run(host="0.0.0.0")
