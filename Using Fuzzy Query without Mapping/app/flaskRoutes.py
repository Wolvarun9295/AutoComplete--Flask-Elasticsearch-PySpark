from app import app
from flask import render_template, request
import requests


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html", title='AutoSuggest')


@app.route('/ajax_call', methods=["GET", "POST"])
def ajax_call():
    data = request.form.get("data")
    url = "http://0.0.0.0:5000/autocomplete?query=" + str(data)
    response = requests.request("GET", url)
    return response.json()
