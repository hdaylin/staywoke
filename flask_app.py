
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buy')
def buy():
    return render_template('buy.html')

@app.route('/art')
def art():
    return render_template('art.html')

@app.route('/activism')
def activism():
    return render_template('activism.html')

@app.route('/food')
def food():
    return render_template('food.html')



