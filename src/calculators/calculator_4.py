from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
  def __init__(self, driver_handle: DriverHandlerInterface) -> None:
    self.__driver_handle = driver_handle

  def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
    body = request.json
    input_data = self.__validate_body(body)
    calculated_number = self.__process_data(input_data)
    formated_response = self.__formated_response(calculated_number)

    return formated_response

  def __formated_response(self, calculated_number:float) -> Dict:
    return {
      "data": {
        "calculator": 4,
        "media": round(calculated_number,2)
      }
    }

  def __process_data(self, input_data: List[float]) -> float:
    result = self.__driver_handle.median(input_data)
    return result

  def __validate_body(self, body: Dict) -> List[float]:
    if "numbers" not in body:
      raise HttpUnprocessableEntityError("Body mal formatado")
    
    input_data = body["numbers"]
    return input_data