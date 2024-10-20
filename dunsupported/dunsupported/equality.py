from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedEquality(UnsupportedOperation):
    @staticmethod
    def equality_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedEquality.unary_operation_not_supported(
                "eq", "=", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def inequality_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedEquality.unary_operation_not_supported(
                "ne", "!=", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def neither_equality_nor_inequality_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedEquality.equality_not_supported(
                message, error_type)(cls)

            cls = UnsupportedEquality.inequality_not_supported(
                message, error_type)(cls)
            return cls

        return decorator
