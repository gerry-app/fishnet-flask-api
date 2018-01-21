from flask import Flask, render_template, redirect, jsonify
import json

app = Flask(__name__)

@app.route('/')
def root():
    return

@app.route('/state/<name>', methods=['GET','POST'])
def get_data(name):
    with open('static/population.json') as dt:
        data = json.load(dt)
    return jsonify(data.get(name))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
