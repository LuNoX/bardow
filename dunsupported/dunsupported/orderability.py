from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedOrderability(UnsupportedOperation):
    @staticmethod
    def less_than_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedOrderability.operation_not_supported(
                "lt", "<", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def less_than_equal_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedOrderability.operation_not_supported(
                "le", "<=", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def greater_than_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedOrderability.operation_not_supported(
                "lt", ">", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def greater_than_equal_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedOrderability.operation_not_supported(
                "le", ">=", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def orderability_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedOrderability.less_than_not_supported(
                message, error_type)(cls)
            cls = UnsupportedOrderability.less_than_equal_not_supported(
                message, error_type)(cls)
            cls = UnsupportedOrderability.greater_than_not_supported(
                message, error_type)(cls)
            cls = UnsupportedOrderability.greater_than_equal_not_supported(
                message, error_type)(cls)
            return cls

        return decorator
