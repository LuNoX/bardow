from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedBitwise(UnsupportedOperation):
    @staticmethod
    def bitwise_and_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedBitwise.operation_not_supported(
                "and", "&", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def bitwise_or_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedBitwise.operation_not_supported(
                "or", "|", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def bitwise_xor_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedBitwise.operation_not_supported(
                "xor", "^", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def bitwise_rshift_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedBitwise.operation_not_supported(
                "rshift", ">>", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def bitwise_lshift_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedBitwise.operation_not_supported(
                "lshift", "<<", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def bitwise_operations_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedBitwise.bitwise_and_not_supported(
                message, error_type)(cls)
            cls = UnsupportedBitwise.bitwise_or_not_supported(
                message, error_type)(cls)
            cls = UnsupportedBitwise.bitwise_xor_not_supported(
                message, error_type)(cls)
            cls = UnsupportedBitwise.bitwise_rshift_not_supported(
                message, error_type)(cls)
            cls = UnsupportedBitwise.bitwise_lshift_not_supported(
                message, error_type)(cls)
            return cls

        return decorator
