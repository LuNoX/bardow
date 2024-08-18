from __future__ import annotations
from typing import TYPE_CHECKING

from bardow.backend import variable, backend

if TYPE_CHECKING:
    from bardow.model import variable as variable_model


class StubVariableRepresentation(variable.VariableBackendRepresentation):
    pass


class StubVariable(variable.VariableBackend):
    def create_backend_representation(
            self, var: variable_model.Variable
    ) -> variable.VariableBackendRepresentation:
        return StubVariableRepresentation()

    def formula_representation(
            self,
            backend_representation: variable.VariableBackendRepresentation
    ) -> str:
        raise NotImplementedError()
