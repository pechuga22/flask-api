from flask import Flask


app = Flask(__name__)
#tengo que importar las rutas debajo de el app, porque todavia no se como ejecutar tareas en segundo plano haha
from flaskblog.routes import routes 
##---directorio-directorio---archivo
#print('init', __name__)