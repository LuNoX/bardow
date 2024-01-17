from dataclasses import dataclass
from abc import ABC, abstractmethod

from bardow.model import units


@dataclass
class Variable(ABC):
    name: str

    @property
    @abstractmethod
    def formula_representation(self) -> str:
        return self.name


@dataclass
class Known(Variable):
    var_unit: units.Unit
    value: float
    # TODO: proper formatting
    representation_format: str = "{value} {var_unit}"

    def formula_representation(self) -> str:
        return self.representation_format.format(value=self.value,
                                                 var_unit=self.var_unit)

    def convert_to(self, unit: units.Unit) -> None:
        factor = self.var_unit.convert_to(unit)
        self.value *= factor
        self.var_unit = unit


@dataclass
class Unknown(Variable):
    symbol: str

    def formula_representation(self) -> str:
        return self.symbol
