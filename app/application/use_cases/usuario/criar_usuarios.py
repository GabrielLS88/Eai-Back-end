
from app.infrastructure.database.usuario.usario_service import create_user

def receber_dados_para_criacao(body):
    if not body.get("nome") or not body.get("email") or not body.get("senha") or not body.get("empresa"):
        return {
            "status": False,
            "mensagem": "Alguns dados não foram passados de acordo com o esperado."
        }
   
    response_criacao = create_user(body)
    return response_criacao