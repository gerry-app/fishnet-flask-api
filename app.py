from flask import Flask, render_template, redirect, jsonify, request
import json
import re

app = Flask(__name__)

@app.route('/')
def root():
    return

@app.route('/state/<name>', methods=['GET','POST'])
def get_data(name):
    with open('static/population.json') as dt:
        data = json.load(dt)
    return jsonify(data.get(name))

URL_PATTERN = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

@app.route('/current-events', methods=['GET', 'POST'])
def current_events():
    if request.method == 'POST':
        url = request.form.get('url', '')
        if re.search(URL_PATTERN, url):
            with open('static/current-events.txt', 'a') as news:
                news.write(url + '\n')
            return jsonify(response=True)
        return jsonify(response=False, url=url)
    with open('static/current-events.txt') as news:
        data = news.read().split('\n')[:-1]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
