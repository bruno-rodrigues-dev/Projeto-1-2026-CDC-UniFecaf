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