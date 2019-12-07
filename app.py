#!/usr/bin/env python

from pprint import pprint as pp

import requests
from flask import Flask, flash, redirect, render_template, request, url_for

from weather import query_api

app = Flask(__name__)


@app.route('/')
def index():
    cities = []
    temp = []
    cities_API_URI = 'https://restcountries.eu/rest/v2/all'
    response = requests.get(cities_API_URI).json()

    for data in response:
        temp.append(data['capital'])

    temp = list(filter(None, temp))
    temp.sort()

    for city in temp:
        cities.append({'name': city})

    return render_template('weather.html', cities=cities)


@app.route("/result", methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
        data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template('result.html', data=data, error=error)


if __name__ == "__main__":
    app.run(debug=True)
