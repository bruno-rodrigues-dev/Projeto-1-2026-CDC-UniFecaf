from app import app
from flask import render_template, redirect
from flask import request, url_for
from banco_de_dados.database import ligar_banco

@app.route("/")
def homepage():
    db = ligar_banco()
    cursor = db.cursor(dictionary=True)
    
    sql = """
        SELECT p.id, p.nome, p.descricao, p.valor, c.nome_categoria, m.nome_marca
        FROM produtos p
        INNER JOIN categorias c ON p.categoria_id = c.id
        INNER JOIN marcas m ON p.marca_id = m.id
        order by p.id
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
        marca_id = request.form["marca"]
        db = ligar_banco()
        cursor = db.cursor()
        sql = "INSERT INTO produtos (nome, descricao, valor, categoria_id, marca_id) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (nome, descricao, preco, cat_id, marca_id))
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
        marca_id = request.form["marca"]
        sql = "UPDATE produtos SET nome=%s, descricao=%s, valor=%s, categoria_id=%s, marca_id=%s WHERE id=%s"
        cursor.execute(sql, (nome, descricao, preco, cat_id, marca_id, id))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for("homepage"))
    
    sql = """
        SELECT p.id, p.nome, p.descricao, p.valor, p.categoria_id, p.marca_id, c.nome_categoria, m.nome_marca
        FROM produtos p
        INNER JOIN categorias c ON p.categoria_id = c.id
        INNER JOIN marcas m ON p.marca_id = m.id
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

@app.route("/pesquisa")
def pesquisa():
    pesquisa = request.args.get("pesquisa")

    db = ligar_banco()
    cursor = db.cursor(dictionary=True)

    sql = """
        SELECT p.id, p.nome, p.descricao, p.valor, p.categoria_id, c.nome_categoria, m.nome_marca
        FROM produtos p
        INNER JOIN categorias c ON p.categoria_id = c.id
        INNER JOIN marcas m ON p.marca_id = m.id
        WHERE p.nome like %s
    """
    cursor.execute(sql, (f"%{pesquisa}%",))

    produtos = cursor.fetchall()
    cursor.close()
    db.close()
    
    return render_template("homepage.html", lista=produtos)