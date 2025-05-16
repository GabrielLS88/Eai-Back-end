from flask import Blueprint, jsonify
from app.application.use_cases.buscar_usuarios import buscar_usuarios

rotas_bp = Blueprint("rotas", __name__)

@rotas_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():
    puxando_usuarios = buscar_usuarios()
    return jsonify(puxando_usuarios)
