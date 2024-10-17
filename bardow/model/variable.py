from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional, override

from sympy.physics import units
from sympy.physics.units import dimensions

from bardow.backend import variable
from bardow.backend.default import DEFAULT_BACKEND
from bardow.backend.backend import backend, HasBackend


@dataclass(kw_only=True)
class Variable(HasBackend, ABC):
    name: str
    dimension: Optional[dimensions.Dimension] = None

    @property
    @abstractmethod
    def is_known(self) -> bool:
        raise NotImplementedError()

    @property
    def formula_representation(self) -> str:
        return self._backend.formula_representation(
            self._backend_representation)


@dataclass(kw_only=True)
@backend(DEFAULT_BACKEND.known)
class Known(Variable):
    unit: units.Unit
    value: float
    symbol: Optional[str] = None

    def __post_init__(self) -> None:
        if self.dimension is not None:
            return
        self.dimension = self.unit.dimension

    @property
    @override
    def is_known(self) -> bool:
        return isinstance(self, Known)


@dataclass(kw_only=True)
@backend(DEFAULT_BACKEND.unknown)
class Unknown(Variable):
    symbol: str

    @property
    @override
    def is_known(self) -> bool:
        return isinstance(self, Known)

    def create_known(self, value: float, unit: units.Unit) -> Known:
        known = Known(
            name=self.name,
            unit=unit,
            value=value,
            symbol=self.symbol,
            _backend=self._backend.known_backend
        )
        return known
