from app.infrastructure.database.usuario.usario_service import update_user

def atalizar_usuario_bd(body):
    if not body.get("nome") or not body.get("email") or not body.get("senha") or not body.get("empresa"):
        return {
            "status": False,
            "mensagem": "Alguns dados não foram passados de acordo com o esperado."
        }
    
    respnose_update = update_user(body)
    return respnose_update