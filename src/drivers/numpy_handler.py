import numpy
from typing import List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class NumpyHandler(DriverHandlerInterface):
  def __init__(self) -> None:
    self.__np = numpy

  def median(self, numbers: List[float]) -> float:
    return self.__np.median(numbers)