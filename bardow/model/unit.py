from dataclasses import dataclass
from typing import Optional, Self, TypeVar, Type, Callable
from numbers import Real

from bardow.backend.default import DEFAULT_BACKEND
from bardow.backend.backend import HasBackend, backend


@dataclass(kw_only=True)
@backend(DEFAULT_BACKEND.dimension)
class Dimension(HasBackend):
    name: str

    # TODO: implement
    def __eq__(self, other: Self) -> bool:
        return self._backend_representation == other._backend_representation

    def __mul__(self, other: Self) -> Self:
        ...

    def __rmul__(self, other: Self) -> Self:
        ...

    def __truediv__(self, other: Self) -> Self:
        ...

    def __rtruediv__(self, other: Self) -> Self:
        ...


@dataclass(kw_only=True)
@backend(DEFAULT_BACKEND.unit)
class Unit(HasBackend):
    name: str
    dimension: Dimension
    formula_representation: str

    # TODO: implement
    def __eq__(self, other: Self) -> bool:
        ...

    def __mul__(self, other: Self | Real) -> Self:
        ...

    def __rmul__(self, other: Self | Real) -> Self:
        ...

    def __imul__(self, other):
        raise TypeError

    def __add__(self, other):
        raise TypeError

    def __iadd__(self, other):
        raise TypeError

    def __radd__(self, other):
        raise TypeError

    def __sub__(self, other):
        raise TypeError

    def __rsub__(self, other):
        raise TypeError

    def __isub__(self, other):
        raise TypeError

    def __truediv__(self, other: Self | Real) -> Self:
        ...

    def __rtruediv__(self, other: Self | Real) -> Self:
        ...

    def __itruediv__(self, other):
        raise TypeError

    def __floordiv__(self, other: Self | Real) -> Self:
        ...

    def __rfloordiv__(self, other: Self | Real) -> Self:
        ...

    def ifloordiv(self, other: Self):
        raise TypeError

    def __neg__(self) -> Self:
        ...

    def __bool__(self) -> bool:
        ...

    def __floor__(self) -> Self:
        ...

    def __lt__(self, other: Self | Real) -> bool:
        ...

    def __pow__(self, power, modulo=None):
        ...

    def __ipow__(self, other):
        raise TypeError

    def __rpow__(self, other):
        ...

    def __xor__(self, other):
        raise TypeError

    def __and__(self, other):
        raise TypeError

    def __or__(self, other):
        raise TypeError

    def __not__(self):
        raise TypeError
