from __future__ import annotations
from dataclasses import dataclass
from typing import override, TYPE_CHECKING, Set, Type

import sympy
from sympy.physics import units
from sympy.physics.units import systems

from bardow.model import errors
from bardow.backend import backendtypes, equation, variable as variable_backend

if TYPE_CHECKING:
    from bardow.model import variable, variablerelationship


@dataclass
class SympyKnownRepresentation(variable_backend.KnownBackendRepresentation):
    quantity: units.Quantity

    @override
    def value(self) -> units.Quantity:
        return self.quantity


class SympyKnown(variable_backend.KnownBackend):
    @classmethod
    def BACKEND_REPRESENTATION(cls) -> Type[SympyKnownRepresentation]:
        return SympyKnownRepresentation

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


SYMPY_KNOWN = SympyKnown()


@dataclass
class SympyUnknownRepresentation(variable_backend.UnknownBackendRepresentation
                                 ):
    symbol: sympy.Symbol

    @override
    def value(self) -> sympy.Symbol:
        return self.symbol


class SympyUnknown(variable_backend.UnknownBackend):
    @classmethod
    def BACKEND_REPRESENTATION(cls) -> Type[SympyUnknownRepresentation]:
        return SympyUnknownRepresentation

    @property
    def known_backend(self) -> SympyKnown:
        return SYMPY_KNOWN

    def create_backend_representation(
            self, unknown: variable.Unknown
    ) -> variable_backend.UnknownBackendRepresentation:
        symbol = sympy.Symbol(unknown.symbol)
        return SympyUnknownRepresentation(symbol)

    def formula_representation(
            self, backend_representation: SympyUnknownRepresentation) -> str:
        return backend_representation.symbol.name


SYMPY_UNKNOWN = SympyUnknown()


@dataclass
class SympyEquationRepresentation(equation.EquationBackendRepresentation):
    equation: sympy.Eq

    @override
    def solve(self, variables: Set[variable.Variable]) -> Set[variable.Known]:
        # TODO: make this nice, right now backend and frontend are coupled
        unknowns = {var for var in variables if not var.is_known}
        if len(unknowns) != 1:
            # If there are 0 unknowns, there is nothing to solve
            # If there is more than one unknown, the equation is not solvable.
            raise errors.NotSolvableError()
        solutions = sympy.solve(self.equation, unknowns)
        knowns = set()
        for unknown, solution in zip(unknowns, solutions.values):
            value, unit = units.convert_to(solution, systems.SI._base_units)
            known = unknown.create_known(value, unit)
            knowns.add(known)
            variables.remove(unknown)
            variables.add(known)
        return knowns

    @override
    def value(self) -> sympy.Eq:
        return self.equation


class SympyEquation(equation.EquationBackend):
    @classmethod
    def BACKEND_REPRESENTATION(
            cls) -> Type[equation.EquationBackendRepresentation]:
        return equation.EquationBackendRepresentation

    @override
    def create_backend_representation(
            self, eq: variablerelationship.Equation
    ) -> equation.EquationBackendRepresentation:
        sympy_equation = sympy.Eq(eq.left_hand_side, eq.right_hand_side)
        return SympyEquationRepresentation(sympy_equation)


SYMPY_EQUATION = SympyEquation()

SYMPY_BACKEND = backendtypes.PartialBackend(
    known=SYMPY_KNOWN,
    unknown=SYMPY_UNKNOWN,
    equation=SYMPY_EQUATION
)
