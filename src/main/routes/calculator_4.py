from flask import Blueprint, request, jsonify
from src.main.factories.calculator_4_factory import calculator4_factory
from src.errors.error_controller import handle_errors

calc_routes_bp = Blueprint("calc_routes", __name__)

@calc_routes_bp.route("/calculator/4", methods=['POST'])
def calculator_4():
  
  try:

    calc = calculator4_factory()
    response = calc.calculate(request)
    return jsonify(response), 200
  
  # tratamento de erros
  except Exception as exception:
    error_response = handle_errors(exception)
    return jsonify(error_response["body"]), error_response["status_code"]