import os
import sqlite3

def usario_service():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'eai.db')
    print(f"Tentando abrir banco: {db_path}")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    resultados = cursor.fetchall()

    conn.close()

    usuarios = [
        {"id": row[0], "nome": row[1], "email": row[2], "senha": row[3], "empresa": row[4]}
        for row in resultados
    ]

    return usuarios
