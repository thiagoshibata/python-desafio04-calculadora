from abc import ABC, abstractmethod
from typing import List

class DriverHandlerInterface(ABC):

  @abstractmethod
  def median(self, numbers: List[float]) -> float:
    pass