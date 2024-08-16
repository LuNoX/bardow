from dataclasses import dataclass, field
from typing import Set

from bardow.model import variablerelationship, variable


@dataclass
class SystemOfRelationships:
    relationships: Set[variablerelationship.VariableRelationship]
    variables: Set[variable.Variable] = field(default_factory=set)

    def __post_init__(self) -> None:
        if self.variables:
            return
        for relationship in self.relationships:
            self.variables += relationship.variables

    def solve(self) -> Set[variable.Known]:
        # TODO: implement
        ...
