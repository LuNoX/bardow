from typing import TypeVar, Callable, Type

T = TypeVar("T")


class UnsupportedOperation:
    DEFAULT_MESSAGE = "Unsupported operation {} for Type: {}"

    @staticmethod
    def set_default_message(message: str) -> None:
        UnsupportedOperation.DEFAULT_MESSAGE = message

    @staticmethod
    def _operation_not_supported(
            prefix: str, operation_name: str, operation_symbol: str = None,
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        if operation_symbol is None:
            operation_symbol = operation_name
        if message is None:
            message = UnsupportedOperation.DEFAULT_MESSAGE
        if error_type is None:
            error_type = TypeError

        def decorator(cls: Type[T]
                      ) -> Type[T]:
            def error(self: cls, *args, **kwargs) -> None:
                raise error_type(message.format(operation_symbol, cls))

            setattr(cls, f"__{prefix}{operation_name}__", error)
            return cls

        return decorator

    @staticmethod
    def operation_default_not_supported(
            operation_name: str,
            operation_symbol: str = None,
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        return UnsupportedOperation._operation_not_supported(
            "", operation_name, operation_symbol, message, error_type)

    @staticmethod
    def operation_left_side_not_supported(
            operation_name: str,
            operation_symbol: str = None,
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        return UnsupportedOperation.operation_default_not_supported(
            operation_name, operation_symbol, message, error_type)

    @staticmethod
    def operation_right_side_not_supported(
            operation_name: str,
            operation_symbol: str = None,
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        return UnsupportedOperation._operation_not_supported(
            "r", operation_name, operation_symbol, message, error_type)

    @staticmethod
    def operation_in_place_not_supported(
            operation_name: str,
            operation_symbol: str = None,
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        return UnsupportedOperation._operation_not_supported(
            "i", operation_name, operation_symbol, message, error_type)

    @staticmethod
    def unary_operation_not_supported(
            operation_name: str,
            operation_symbol: str = None,
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        return UnsupportedOperation.operation_default_not_supported(
            operation_name, operation_symbol, message, error_type)

    @staticmethod
    def binary_operation_not_supported(
            operation_name: str,
            operation_symbol: str = None,
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]
                      ) -> Type[T]:
            cls = UnsupportedOperation.operation_default_not_supported(
                operation_name, operation_symbol, message, error_type)(cls)
            cls = UnsupportedOperation.operation_right_side_not_supported(
                operation_name, operation_symbol, message, error_type)(cls)
            cls = UnsupportedOperation.operation_in_place_not_supported(
                operation_name, operation_symbol, message, error_type)(cls)
            return cls

        return decorator

    @staticmethod
    def operation_not_supported(
            operation_name: str,
            operation_symbol: str = None,
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        return UnsupportedOperation.binary_operation_not_supported(
            operation_name, operation_symbol, message, error_type)
