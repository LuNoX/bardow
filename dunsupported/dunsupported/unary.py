from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedUnary(UnsupportedOperation):
    @staticmethod
    def negation_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedUnary.unary_operation_not_supported(
                "neg", "-", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def positive_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedUnary.unary_operation_not_supported(
                "pos", "+", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def inverse_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedUnary.unary_operation_not_supported(
                "invert", "~", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def unary_operations_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedUnary.negation_not_supported(
                message, error_type)(cls)
            cls = UnsupportedUnary.positive_not_supported(
                message, error_type)(cls)
            cls = UnsupportedUnary.inverse_not_supported(
                message, error_type)(cls)
            return cls

        return decorator
