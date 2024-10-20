from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedLifetimeManagement(UnsupportedOperation):
    @staticmethod
    def creation_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedLifetimeManagement.unary_operation_not_supported(
                "new", f'{cls.__name__}(...)', message, error_type
            )(cls)

        return decorator

    @staticmethod
    def initialisation_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedLifetimeManagement.unary_operation_not_supported(
                "init", f'{cls.__name__}(...)', message, error_type
            )(cls)

        return decorator

    @staticmethod
    def deletion_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedLifetimeManagement.unary_operation_not_supported(
                "del", f'del {cls.__name__}', message, error_type
            )(cls)

        return decorator

    @staticmethod
    def context_management_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedLifetimeManagement.creation_not_supported(
                message, error_type)(cls)

            cls = UnsupportedLifetimeManagement.initialisation_not_supported(
                message, error_type)(cls)
            cls = UnsupportedLifetimeManagement.deletion_not_supported(
                message, error_type)(cls)
            return cls

        return decorator
