import mysql.connector # Use assim

def ligar_banco():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='2007Pedro@',
            database='projeto_unifecaf'
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Erro ao conectar: {e}")
        return None
    
def validarCat(categoria):
    db = ligar_banco()
    cursor = db.cursor(dictionary=True)

    categoria = categoria.strip().title()

    sql = """
        SELECT id
        from categorias 
        where nome_categoria = %s
    """
    cursor.execute(sql, (categoria,))

    categoria_val = cursor.fetchone()

    if not categoria_val:
        sql = """
        INSERT INTO categorias (nome_categoria)
        VALUES (%s)
    """
        cursor.execute(sql, (categoria,))
        db.commit()
        categoria_id = cursor.lastrowid

    else:
        categoria_id = categoria_val["id"]

    cursor.close()
    db.close()
    return categoria_id 


def validarMarca(marca):
    db = ligar_banco()
    cursor = db.cursor(dictionary=True)

    marca = marca.strip().title()

    sql = """
        SELECT id
        from marcas 
        where nome_marca = %s
    """
    cursor.execute(sql, (marca,))

    marca_val = cursor.fetchone()

    if not marca_val:
        sql = """
        INSERT INTO marcas (nome_marca)
        VALUES (%s)
    """
        cursor.execute(sql, (marca,))
        db.commit()
        marca_id = cursor.lastrowid

    else:
        marca_id = marca_val["id"]

    cursor.close()
    db.close()
    return marca_id

    