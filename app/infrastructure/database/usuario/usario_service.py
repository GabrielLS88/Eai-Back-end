import os
import sqlite3


def get_user():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
    db_path = os.path.join(base_dir, 'eai.db')
    conn = sqlite3.connect(db_path, timeout=10)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    resultados = cursor.fetchall()
    conn.close()
    usuarios = [
        {"id": row[0], "nome": row[1], "email": row[2], "senha": row[3], "empresa": row[4]}
        for row in resultados
    ]

    return usuarios


def create_user(dados):
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
        db_path = os.path.join(base_dir, 'eai.db')
        nome = dados.get("nome")
        email = dados.get("email")
        senha = dados.get("senha")
        empresa = dados.get("empresa")
        
        conn = sqlite3.connect(db_path, timeout=10)
        cursor = conn.cursor()
        
        insert = "INSERT INTO usuarios (nome, email, senha, empresa) VALUES (?, ?, ?, ?)"
        cursor.execute(insert, (nome, email, senha, empresa))
        
        conn.commit()
        novo_id = cursor.lastrowid
        conn.close()
        
        return {
            "status": True,
            "mensagem": "Usuário criado com sucesso.",
            "id_usuario": novo_id
        }

    except Exception as e:
        return {
            "status": False,
            "mensagem": f"Erro ao criar usuário: {str(e)}"
        }


def update_user(dados):
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
        db_path = os.path.join(base_dir, 'eai.db')
        nome = dados.get("nome")
        email = dados.get("email")
        senha = dados.get("senha")
        empresa = dados.get("empresa")
        
        conn = sqlite3.connect(db_path, timeout=10)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        consultaCliente = cursor.fetchone()
        
        if not consultaCliente:
            return {
                "status": False,
                "mensagem": "Usuário não encontrado."
            }
        
        update = "UPDATE usuarios SET nome = ?, email = ?, senha = ?, empresa = ? WHERE email = ?"
        cursor.execute(update, (nome, email, senha, empresa, email))
        
        conn.commit()
        conn.close()
        
        return {
            "status": True,
            "mensagem": "Usuário atualizado com sucesso."
        }
    except Exception as e:
        return {
            "status": False,
            "mensagem": f"Erro ao atualizado usuário: {str(e)}"
        }


def delet_user(idDelete):
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
        db_path = os.path.join(base_dir, 'eai.db')
        
        conn = sqlite3.connect(db_path, timeout=10)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (idDelete,))
        
        conn.commit()
        conn.close()
        
        return {
            "status": True,
            "mensagem": "Usuário apagado com sucesso."
        }
    except Exception as e:
        return {
            "status": False,
            "mensagem": f"Erro ao apagar usuário: {str(e)}"
        }
