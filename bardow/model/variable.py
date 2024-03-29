from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional, overrides

import sympy
from sympy.physics import units
from sympy.physics.units import systems


@dataclass
class Variable(ABC):
    name: str

    @property
    @abstractmethod
    def is_known(self) -> bool:
        raise NotImplementedError

    @property
    @abstractmethod
    def formula_representation(self) -> str:
        raise NotImplementedError


@dataclass
class Known(Variable):
    unit: units.Unit
    value: float
    symbol: Optional[str] = None

    __sympy_quantity: units.Quantity = None

    @property
    def _sympy_quantity(self) -> units.Quantity:
        if self.__sympy_quantity is not None:
            return self.__sympy_quantity
        quantity = units.Quantity(self.name)
        systems.SI.set_quantity_dimension(quantity, self.unit.dimension)
        systems.SI.set_quantity_scale_factor(quantity, self.value * self.unit)
        self.__sympy_quantity = quantity
        return quantity

    @overrides
    def is_known(self) -> bool:
        return True

    @overrides
    def formula_representation(self) -> str:
        return str(self.__sympy_quantity.convert_to(systems.SI._base_units))


@dataclass
class Unknown(Variable):
    symbol: str
    __sympy_symbol: sympy.Symbol = None

    @property
    def _sympy_symbol(self) -> sympy.Symbol:
        if self.__sympy_symbol is not None:
            return self.__sympy_symbol
        symbol = sympy.Symbol(self.symbol)
        self.__sympy_symbol = symbol
        return symbol

    @overrides
    def is_known(self) -> bool:
        return False

    @overrides
    def formula_representation(self) -> str:
        return self.symbol

    def create_known(self, value: float, unit: units.Unit) -> Known:
        known = Known(
            name=self.name,
            unit=unit,
            value=value,
            symbol=self.symbol
        )
        return known
