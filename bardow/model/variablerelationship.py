from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Set, Any, override, Optional

from bardow.model import variable, table as table_
from bardow.backend import equation
from bardow.backend.default import DEFAULT_BACKEND
from bardow.backend.backend import HasBackend


@dataclass(kw_only=True)
class VariableRelationship(ABC):
    variables: Set[variable.Variable]

    @abstractmethod
    def relate(self) -> Set[variable.Known]:
        raise NotImplementedError()


@dataclass(kw_only=True)
class Equation(VariableRelationship, HasBackend):
    left_hand_side: Any
    right_hand_side: Any
    _backend: equation.EquationBackend = DEFAULT_BACKEND.equation
    _backend_representation: Optional[
        equation.EquationBackendRepresentation] = None

    @override
    def relate(self) -> Set[variable.Known]:
        return self._backend_representation.solve(self.variables)


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
