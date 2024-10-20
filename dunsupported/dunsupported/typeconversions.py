from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedTypeConversion(UnsupportedOperation):
    @staticmethod
    def type_conversion_not_supported(
            type_name: str,
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedTypeConversion.unary_operation_not_supported(
                type_name, f"{type_name}(obj)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def string_conversion_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedTypeConversion.type_conversion_not_supported(
                'str', message, error_type
                )(cls)

        return decorator

    @staticmethod
    def boolean_conversion_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedTypeConversion.type_conversion_not_supported(
                'bool', message, error_type
                )(cls)

        return decorator

    @staticmethod
    def integer_conversion_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedTypeConversion.type_conversion_not_supported(
                'int', message, error_type
                )(cls)

        return decorator

    @staticmethod
    def floating_point_conversion_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedTypeConversion.type_conversion_not_supported(
                'float', message, error_type
                )(cls)

        return decorator

    @staticmethod
    def bytes_conversion_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedTypeConversion.type_conversion_not_supported(
                'bytes', message, error_type
                )(cls)

        return decorator

    @staticmethod
    def complex_number_conversion_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedTypeConversion.type_conversion_not_supported(
                'complex', message, error_type
                )(cls)

        return decorator

    @staticmethod
    def type_conversions_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedTypeConversion.string_conversion_not_supported(
                message, error_type)(cls)
            cls = UnsupportedTypeConversion.boolean_conversion_not_supported(
                message, error_type)(cls)
            cls = UnsupportedTypeConversion.integer_conversion_not_supported(
                message, error_type)(cls)
            cls = UnsupportedTypeConversion. \
                floating_point_conversion_not_supported(
                message, error_type)(cls)
            cls = UnsupportedTypeConversion.bytes_conversion_not_supported(
                message, error_type)(cls)
            cls = UnsupportedTypeConversion. \
                complex_number_conversion_not_supported(
                message, error_type)(cls)
            return cls

        return decorator
