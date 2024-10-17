from dataclasses import dataclass
from typing import Optional

from bardow.backend import unit
from bardow.backend.default import DEFAULT_BACKEND
from bardow.backend.backend import HasBackend


@dataclass(kw_only=True)
class Dimension(HasBackend):
    name: str
    _backend: Optional[unit.UnitBackend] = DEFAULT_BACKEND.unit
    __backend_representation: Optional[unit.UnitBackendRepresentation] = None

    def _backend_representation(self) -> unit.UnitBackendRepresentation:
        return super()._backend_representation


@dataclass(kw_only=True)
class Unit(HasBackend):
    name: str
    dimension: Dimension
    formula_representation: str
    _backend: Optional[unit.UnitBackend] = DEFAULT_BACKEND.unit
    __backend_representation: Optional[unit.UnitBackendRepresentation] = None

    def _backend_representation(self) -> unit.UnitBackendRepresentation:
        return super()._backend_representation
