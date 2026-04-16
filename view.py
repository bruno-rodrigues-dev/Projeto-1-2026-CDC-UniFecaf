from main import app


# rotas
@app.route("/")
def homepage():
    return "Commercia - Seja Bem-Vindo"

@app.route("/blog")
def blog():
    return "Seja Bem-Vindo ao Blog"