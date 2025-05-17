from flask import Blueprint, request, jsonify
from app.application.use_cases.usuario.buscar_usuarios import buscar_usuarios
from app.application.use_cases.usuario.criar_usuarios import receber_dados_para_criacao
from app.application.use_cases.usuario.atualizar_usuario import update_user
from app.application.use_cases.usuario.apagar_usuario import apagar_usuario

rotas_bp = Blueprint("rotas", __name__)

@rotas_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():
    puxando_usuarios = buscar_usuarios()
    return jsonify(puxando_usuarios)


@rotas_bp.route("/usuarios", methods=["POST"])
def criar_usuario():
    body = request.get_json()
    response_criacao = receber_dados_para_criacao(body)
    return jsonify(response_criacao)



@rotas_bp.route("/usuarios", methods=["PUT"])
def update_usuario():
    body = request.get_json()
    response_update = update_user(body)
    return jsonify(response_update)


@rotas_bp.route("/usuarios", methods=["DELETE"])
def deletar_usuario():
    idDelete = request.args.get("id")
    response = apagar_usuario(idDelete)
    return jsonify(response)
