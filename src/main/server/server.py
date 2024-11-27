from flask import Flask
from src.main.routes.calculator_4 import calc_routes_bp

app = Flask(__name__)

app.register_blueprint(calc_routes_bp)