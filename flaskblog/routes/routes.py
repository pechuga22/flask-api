from flaskblog import app

@app.route('/saludo')
def home():
    return 'Hello World'

@app.route('/')
def home1():
    return 'princip[al]'    