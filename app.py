from Flask import flask, render_template, redirect
import json

app = Flask(__name__)

@app.route('/')
def root():
    return

@app.route('/state/<name>', methods=['GET','POST'])
def get_data(name):
    with open('static/population.json') as dt:
        data = json.load(dt)
    return data[name]
    

if __name__ == '__main__':
    app.run()
