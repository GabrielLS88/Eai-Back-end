#buscar_usuarios
from app.infrastructure.database.usuario.usario_service import get_user

def buscar_usuarios():
    consulta_usuarios = get_user()
    return consulta_usuarios