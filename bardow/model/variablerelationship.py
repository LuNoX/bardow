from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List

from bardow.model import variable


@dataclass
class VariableRelationship(ABC):
    variables: List[variable.Variable]

    @abstractmethod
    def relate(self) -> None:
        pass


@dataclass
class Equation(VariableRelationship):
    pass


@dataclass
class Function(Equation):
    pass


@dataclass
class ValueTable(VariableRelationship):
    pass
