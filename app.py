from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Grupo 10 - Hello World"

if __name__ == '__main__':
    app.run()
