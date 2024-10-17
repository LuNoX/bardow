from dataclasses import dataclass, fields
from typing import Optional, Self

from bardow.backend import variable, equation as equation_


# TODO: give this a proper name!

# TODO: add dimensions
# TODO: add units
# TODO: add WaterProperties


@dataclass
class BackendTypes:
    known: variable.KnownBackend
    unknown: variable.UnknownBackend
    equation: equation_.EquationBackend


@dataclass
class PartialBackend(BackendTypes):
    known: Optional[variable.KnownBackend] = None
    unknown: Optional[variable.UnknownBackend] = None
    equation: Optional[equation_.EquationBackend] = None

    def is_complete(self) -> bool:
        return all(
            (getattr(self, field.name) for field in fields(BackendTypes)))

    def __add__(self, other: Self) -> Self:
        self.known = other.known or self.known
        self.unknown = other.unknown or self.unknown
        self.equation = other.equation or self.equation
        return self

    def __or__(self, other: Self) -> Self:
        return self.__add__(other)


def test():
    # TODO: move this test to proper testing classes
    variable.KnownBackend.__abstractmethods__ = set()
    variable.UnknownBackend.__abstractmethods__ = set()
    known = variable.KnownBackend()
    unknown = variable.UnknownBackend()
    p1 = PartialBackend(known=known)
    print(p1.is_complete())
    p2 = PartialBackend(unknown=unknown)
    print(p2.is_complete())
    p3 = p1 + p2
    print(p3)
    print(p3.is_complete())


if __name__ == "__main__":
    test()
