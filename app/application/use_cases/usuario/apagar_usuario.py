from app.infrastructure.database.usuario.usario_service import delet_user

def apagar_usuario(idDelete):
    if not idDelete:
        return {
            "status": False,
            "mensagem": "O id não foi passado de acordo com o esperado."
        }
    
    respnose_delet = delet_user(idDelete)
    return respnose_delet