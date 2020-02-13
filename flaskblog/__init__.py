from flask import Flask


app = Flask(__name__)
from flaskblog import routes

#print('init', __name__)