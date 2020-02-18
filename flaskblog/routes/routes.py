from flaskblog import app
from flask import render_template

@app.route('/')
def home():
    posts = [
        {
            "title":"First Content",
            "description" : "First Description"
        },
        {
            "title":"Second Content",
            "description" : "Second Description"
        },
        {
            "title":"Third Content",
            "description" : "Third Description"
        }
    ]
    return render_template('index.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')    