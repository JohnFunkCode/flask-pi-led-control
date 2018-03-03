from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def main_page():
    return render_template('index.html')

@app.route('/individual.html')
def individual_page():
    return render_template('individual.html')

@app.route('/group.html')
def group_page():
    return render_template('group.html')

@app.route('/patterns.html')
def patterns_page():
    return render_template('patterns.html')
