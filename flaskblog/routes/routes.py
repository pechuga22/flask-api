from flaskblog import app
from flask import render_template

@app.route('/saludo')
def home():
    return render_template('index.html')

@app.route('/')
def home1():
    return 'princip[al]'    