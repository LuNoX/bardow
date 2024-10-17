from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, override, TYPE_CHECKING

from bardow.backend import backend
from bardow.backend.backend import HasBackend, BackendRepresentation

if TYPE_CHECKING:
    from bardow.model import unit


class UnitBackendRepresentation(backend.BackendRepresentation, ABC):
    @property
    @abstractmethod
    def dimension(self):
        raise NotImplementedError()

    @override
    def value(self) -> Any:
        pass


class UnitBackend(backend.BackendImplementation, ABC):
    @override
    def create_backend_representation(self, obj: unit.Unit
                                      ) -> UnitBackendRepresentation:
        pass
