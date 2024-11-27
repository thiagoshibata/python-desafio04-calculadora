from typing import Dict, List
from .calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

class MockDriverHandler:
  def median(self, numbers: List[float]) -> float:
    return 3

def test_calculate():
  mock_request = MockRequest({"numbers":[1,2,3,4,5]})
  driver = MockDriverHandler()
  calculator_4 = Calculator4(driver)

  formated_response = calculator_4.calculate(mock_request)

  assert formated_response == {'data': {'calculator': 4, 'media': 3}}
  assert isinstance(formated_response, dict)

def test_calculate_integrate():
  mock_request = MockRequest({"numbers":[5,5]})
  driver = NumpyHandler()
  calculator_4 = Calculator4(driver)

  formated_response = calculator_4.calculate(mock_request)

  assert formated_response == {'data': {'calculator': 4, 'media': 5}}
  assert isinstance(formated_response, dict)