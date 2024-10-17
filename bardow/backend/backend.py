from __future__ import annotations
from typing import Optional, Any, Type, TypeVar, Callable
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class BackendRepresentation(ABC):
    @property
    @abstractmethod
    def value(self) -> Any:
        raise NotImplementedError()


class BackendImplementation(ABC):

    @classmethod
    @property
    @abstractmethod
    def BACKEND_REPRESENTATION(cls) -> Type[BackendRepresentation]:
        return BackendRepresentation

    @abstractmethod
    def create_backend_representation(self, obj: HasBackend
                                      ) -> BackendRepresentation:
        raise NotImplementedError()


@dataclass
class HasBackend(ABC):
    """
    Mixin class for TypeHints
    Only meant to be used in conjunction with @backend
    """
    _backend: BackendImplementation
    _backend_representation_property: Optional[BackendRepresentation] = None

    @property
    # @abstractmethod
    # should be abstract and works fine but PyCharm will complain everywhere
    def _backend_representation(self) -> BackendRepresentation:
        raise NotImplementedError()


_HasBackend = TypeVar('_HasBackend')


def backend(backend_implementation: BackendImplementation
            ) -> Callable[[Type[_HasBackend]], Type[_HasBackend]]:
    def decorator(cls: Type[_HasBackend]) -> Type[_HasBackend]:
        _backend = '_backend'
        setattr(cls, _backend, field(default=backend_implementation))
        cls.__annotations__[_backend] = backend_implementation.__class__

        _backend_representation_property = '_backend_representation_property'
        setattr(cls, _backend_representation_property, field(default=None))
        cls.__annotations__[
            _backend_representation_property
        ] = backend_implementation.BACKEND_REPRESENTATION

        def get_backend_representation(
                self: cls) -> backend_implementation.BACKEND_REPRESENTATION:
            if self._backend_representation_property is None:
                self._backend_representation_property = self. \
                    _backend.create_backend_representation(self)
            return self._backend_representation_property

        def set_backend_representation(
                self: cls, obj: backend_implementation.BACKEND_REPRESENTATION
        ) -> None:
            self._backend_representation_property = obj

        _backend_representation = property(
            get_backend_representation, set_backend_representation)

        setattr(cls, '_backend_representation', _backend_representation)

        if cls.__doc__ is None:
            cls.__doc__ = ""
        cls.__doc__ += "\n@DynamicAttrs"

        return cls

    return decorator
