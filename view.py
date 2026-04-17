from app import app
from flask import render_template, redirect
from flask import request, url_for


# rotas
lista = []
@app.route("/")
def homepage():
    return render_template("homepage.html", lista=lista)

@app.route("/criar", methods=["POST"])
def criar():
    if request.method == "POST":
        nome = request.form["nome"]
        preco = float(request.form["preco"])

        lista.append({
            "nome": nome, 
            "preco": preco, 
            })

        return redirect(url_for("homepage"))