from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedStringFormatting(UnsupportedOperation):
    @staticmethod
    def format_string_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedStringFormatting.unary_operation_not_supported(
                "format", 'f"{obj:s}"', message, error_type
            )(cls)

        return decorator

    @staticmethod
    def string_representation_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedStringFormatting.unary_operation_not_supported(
                "repr", 'repr(obj)', message, error_type
            )(cls)

        return decorator

    @staticmethod
    def neither_format_string_nor_string_representation_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedStringFormatting.format_string_not_supported(
                message, error_type)(cls)
            cls = UnsupportedStringFormatting. \
                string_representation_not_supported(
                message, error_type)(cls)
            return cls

        return decorator
