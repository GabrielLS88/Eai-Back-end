# main.py
from flask import Flask, jsonify
from app.routes.rotas import rotas_bp

from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)

app.register_blueprint(rotas_bp, url_prefix="/eai")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
