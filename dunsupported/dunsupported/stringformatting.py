from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedStringFormatting(UnsupportedOperation):
    @staticmethod
    def format_string_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedStringFormatting.unary_operation_not_supported(
            "format", 'f"{obj:s}"'
        )(cls)

    @staticmethod
    def string_representation_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedStringFormatting.unary_operation_not_supported(
            "repr", 'repr(obj)'
        )(cls)

    @staticmethod
    def neither_format_string_nor_string_representation_supported(cls: Type[T]
                                                                  ) -> Type[T]:
        cls = UnsupportedStringFormatting.format_string_not_supported(cls)
        cls = UnsupportedStringFormatting.string_representation_not_supported(
            cls)
        return cls
