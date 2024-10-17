from __future__ import annotations
from abc import ABC, abstractmethod
from typing import override, Set, TYPE_CHECKING

from bardow.backend import backend

if TYPE_CHECKING:
    from bardow.model import variable
    from bardow.model import variablerelationship


class EquationBackendRepresentation(backend.BackendRepresentation, ABC):

    @abstractmethod
    def solve(self, variables: Set[variable.Variable]) -> Set[variable.Known]:
        raise NotImplementedError()


class EquationBackend(backend.BackendImplementation, ABC):

    @override
    @abstractmethod
    def create_backend_representation(self, eq: variablerelationship.Equation
                                      ) -> EquationBackendRepresentation:
        raise NotImplementedError()
