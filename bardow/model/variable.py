from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional, override

from sympy.physics import units
from sympy.physics.units import dimensions

from bardow.backend import variable
from bardow.backend.default import DEFAULT_BACKEND


@dataclass(kw_only=True)
class Variable(ABC):
    name: str
    _backend: variable.VariableBackend
    dimension: Optional[dimensions.Dimension] = None
    _backend_representation: Optional[
        variable.VariableBackendRepresentation] = None

    def __post_init__(self) -> None:
        # TODO: consider doing this just in time when accessed instead of
        #  always
        self._backend_representation = self._backend. \
            create_backend_representation(self)

    @property
    @abstractmethod
    def is_known(self) -> bool:
        raise NotImplementedError()

    @property
    def formula_representation(self) -> str:
        return self._backend.formula_representation(
            self._backend_representation)


@dataclass(kw_only=True)
class Known(Variable):
    unit: units.Unit
    value: float
    _backend: Optional[variable.KnownBackend] = DEFAULT_BACKEND.known
    symbol: Optional[str] = None

    @override
    def __post_init__(self) -> None:
        super().__post_init__()
        self.dimension = self.unit.dimension

    @property
    @override
    def is_known(self) -> bool:
        return isinstance(self, Known)


@dataclass(kw_only=True)
class Unknown(Variable):
    symbol: str
    _backend: Optional[variable.UnknownBackend] = DEFAULT_BACKEND.unknown

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
