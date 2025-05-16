#buscar_usuarios
from app.infrastructure.database.usario_service import usario_service

def buscar_usuarios():
    consulta_usuarios = usario_service()
    return consulta_usuarios