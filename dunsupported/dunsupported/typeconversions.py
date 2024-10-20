from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedTypeConversion(UnsupportedOperation):
    @staticmethod
    def type_conversion_not_supported(cls: Type[T], type_name: str) -> Type[T]:
        return UnsupportedTypeConversion.unary_operation_not_supported(
            type_name, f"{type_name}(obj)"
        )(cls)

    @staticmethod
    def string_conversion_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedTypeConversion.type_conversion_not_supported(
            cls, 'str')

    @staticmethod
    def boolean_conversion_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedTypeConversion.type_conversion_not_supported(
            cls, 'bool')

    @staticmethod
    def integer_conversion_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedTypeConversion.type_conversion_not_supported(
            cls, 'int')

    @staticmethod
    def floating_point_conversion_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedTypeConversion.type_conversion_not_supported(
            cls, 'float')

    @staticmethod
    def bytes_conversion_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedTypeConversion.type_conversion_not_supported(
            cls, 'bytes')

    @staticmethod
    def complex_number_conversion_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedTypeConversion.type_conversion_not_supported(
            cls, 'complex')

    @staticmethod
    def time_conversions_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedTypeConversion.string_conversion_not_supported(cls)
        cls = UnsupportedTypeConversion.boolean_conversion_not_supported(cls)
        cls = UnsupportedTypeConversion.integer_conversion_not_supported(cls)
        cls = UnsupportedTypeConversion. \
            floating_point_conversion_not_supported(cls)
        cls = UnsupportedTypeConversion.bytes_conversion_not_supported(cls)
        cls = UnsupportedTypeConversion. \
            complex_number_conversion_not_supported(cls)
        return cls
