from flaskblog import app #importo el objeto app para correr el server

if __name__ == '__main__':
    
    app.run(debug=True,host='localhost', port=3000)