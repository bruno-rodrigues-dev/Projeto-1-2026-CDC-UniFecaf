from app import app
from flask import render_template, redirect
from flask import request, url_for
from database import ligar_banco
# sql alchemy

@app.route("/")
def homepage():
    db = ligar_banco()
    cursor = db.cursor(dictionary=True)
    
    sql = """
        SELECT p.id, p.nome, p.descricao, p.valor, c.nome_categoria 
        FROM produtos p
        INNER JOIN categorias c ON p.categoria_id = c.id
    """
    cursor.execute(sql)
    lista_produtos = cursor.fetchall()
    
    cursor.close()
    db.close()
    return render_template("homepage.html", lista=lista_produtos)

@app.route("/criar", methods=["POST"])
def criar():
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        preco = float(request.form["preco"])
        cat_id = request.form["categoria"]
        db = ligar_banco()
        cursor = db.cursor()
        sql = "INSERT INTO produtos (nome, descricao, valor, categoria_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nome, descricao, preco, cat_id))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for("homepage"))

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    db = ligar_banco()
    cursor = db.cursor(dictionary=True)
    
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        preco = float(request.form["preco"])
        cat_id = request.form["categoria"]
        sql = "UPDATE produtos SET nome=%s, descricao=%s, valor=%s, categoria_id=%s WHERE id=%s"
        cursor.execute(sql, (nome, descricao, preco, cat_id, id))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for("homepage"))
    
    sql = """
        SELECT p.id, p.nome, p.descricao, p.valor, p.categoria_id, c.nome_categoria 
        FROM produtos p
        INNER JOIN categorias c ON p.categoria_id = c.id
        WHERE p.id = %s
    """
    cursor.execute(sql, (id,))
    produto = cursor.fetchone()
    
    cursor.close()
    db.close()
    return render_template("editar.html", produto=produto)

@app.route("/deletar/<int:id>")
def deletar(id):
    db = ligar_banco()
    cursor = db.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    db.close()
    return redirect("/")