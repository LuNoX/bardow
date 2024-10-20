from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedLifetimeManagement(UnsupportedOperation):
    @staticmethod
    def creation_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedLifetimeManagement.unary_operation_not_supported(
            "new", f'{cls.__name__}(...)'
        )(cls)

    @staticmethod
    def initialisation_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedLifetimeManagement.unary_operation_not_supported(
            "init", f'{cls.__name__}(...)'
        )(cls)

    @staticmethod
    def deletion_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedLifetimeManagement.unary_operation_not_supported(
            "del", f'del {cls.__name__}'
        )(cls)

    @staticmethod
    def context_management_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedLifetimeManagement.creation_not_supported(cls)
        cls = UnsupportedLifetimeManagement.initialisation_not_supported(cls)
        cls = UnsupportedLifetimeManagement.deletion_not_supported(cls)
        return cls
