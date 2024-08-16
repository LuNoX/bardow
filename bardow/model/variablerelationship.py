from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Set, Any, override

import sympy
from sympy.physics import units
from sympy.physics.units.systems import SI

from bardow.model import variable, errors, table as table_


@dataclass
class VariableRelationship(ABC):
    variables: Set[variable.Variable]

    @abstractmethod
    def relate(self) -> Set[variable.Known]:
        raise NotImplementedError


@dataclass
class Equation(VariableRelationship):
    left_hand_side: Any
    right_hand_side: Any
    __sympy_equation: sympy.Eq = None

    @property
    def _sympy_equation(self) -> sympy.Eq:
        if self.__sympy_equation is not None:
            return self.__sympy_equation
        equation = sympy.Eq(self.left_hand_side, self.right_hand_side)
        self.__sympy_equation = equation
        return equation

    @override
    def relate(self) -> Set[variable.Known]:
        unknowns = {var for var in self.variables if not var.is_known}
        if len(unknowns) != 1:
            # If there are 0 unknowns, there is nothing to solve
            # If there is more than one unknown, the equation is not solvable.

            # TODO: linear systems of equations may be solvable by combining
            #  multiple equations with more than one unknown each
            raise errors.NotSolvableError()
        solutions = sympy.solve(self.__sympy_equation, unknowns)
        knowns = set()
        for unknown, solution in zip(unknowns, solutions.values):
            value, unit = units.convert_to(solution, SI._base_units)
            known = unknown.create_known(value, unit)
            knowns.add(known)
            self.variables.remove(unknown)
            self.variables.add(known)
        return knowns


@dataclass
class Function(Equation):
    left_hand_side = variable.Variable


@dataclass
class ValueTable(VariableRelationship):
    table: table_.Table

    @override
    def relate(self) -> Set[variable.Known]:
        knowns = {var for var in self.variables if var.is_known}
        return self.table.lookup(knowns, only_return=self.variables - knowns)
