from flaskblog import app

@app.route('/saludo')
def home():
    return 'Hello World'