from __future__ import annotations
from abc import ABC, abstractmethod
from typing import override, TYPE_CHECKING

if TYPE_CHECKING:
    from bardow.model import variable


class VariableBackendRepresentation(ABC):
    pass


class VariableBackend(ABC):

    @abstractmethod
    def create_backend_representation(self, var: variable.Variable
                                      ) -> VariableBackendRepresentation:
        raise NotImplementedError()

    @abstractmethod
    def formula_representation(
            self, backend_representation: VariableBackendRepresentation
    ) -> str:
        raise NotImplementedError()


class KnownBackendRepresentation(VariableBackendRepresentation, ABC):
    pass


class KnownBackend(VariableBackend, ABC):

    @override
    @abstractmethod
    def create_backend_representation(self, known: variable.Known
                                      ) -> KnownBackendRepresentation:
        raise NotImplementedError()


class UnknownBackendRepresentation(VariableBackendRepresentation, ABC):
    pass


class UnknownBackend(VariableBackend, ABC):
    @property
    @abstractmethod
    def known_backend(self) -> KnownBackend:
        raise NotImplementedError()

    @override
    @abstractmethod
    def create_backend_representation(self, unknown: variable.Unknown
                                      ) -> UnknownBackendRepresentation:
        raise NotImplementedError()
