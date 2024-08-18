from __future__ import annotations
from dataclasses import dataclass
from typing import Type, TYPE_CHECKING

import sympy
from sympy.physics import units
from sympy.physics.units import systems

from bardow.backend import backend, variable as variable_backend

if TYPE_CHECKING:
    from bardow.model import variable


@dataclass
class SympyKnownRepresentation(variable_backend.KnownBackendRepresentation):
    quantity: units.Quantity


class SympyKnown(variable_backend.KnownBackend):
    def create_backend_representation(self, known: variable.Known
                                      ) -> SympyKnownRepresentation:
        quantity = units.Quantity(known.name)
        systems.SI.set_quantity_dimension(quantity, known.unit.dimension)
        systems.SI.set_quantity_scale_factor(quantity,
                                             known.value * known.unit)
        return SympyKnownRepresentation(quantity)

    def formula_representation(
            self, backend_representation: SympyKnownRepresentation) -> str:
        # TODO: use symbols for units instead of full name?
        return str(backend_representation.quantity.convert_to(
            systems.SI._base_units))


@dataclass
class SympyUnknownRepresentation(variable_backend.UnknownBackendRepresentation
                                 ):
    symbol: sympy.Symbol


class SympyUnknown(variable_backend.UnknownBackend):
    @property
    def known_backend(self) -> Type[SympyKnown]:
        return SympyKnown

    def create_backend_representation(
            self, unknown: variable.Unknown
    ) -> variable_backend.UnknownBackendRepresentation:
        symbol = sympy.Symbol(unknown.symbol)
        return SympyUnknownRepresentation(symbol)

    def formula_representation(
            self, backend_representation: SympyUnknownRepresentation) -> str:
        return backend_representation.symbol.name


SYMPY_BACKEND = backend.PartialBackend(
    known=SympyKnown(),
    unknown=SympyUnknown())
