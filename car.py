from abc import ABC, abstractmethod

from engine.engine import Engine
from battery.battery import Battery

from test.test_car import unittest

class Car(ABC):
    def __init__(self, engine: Engine, battery: Battery) -> None:
        self.engine= engine
        self.battery=battery

    @abstractmethod
    def needs_service(self) -> bool:
        pass

if __name__ == '__main__':
    unittest.main()