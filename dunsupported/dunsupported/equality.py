from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedEquality(UnsupportedOperation):
    @staticmethod
    def equality_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedEquality.unary_operation_not_supported(
            "eq", "="
        )(cls)

    @staticmethod
    def inequality_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedEquality.unary_operation_not_supported(
            "ne", "!="
        )(cls)

    @staticmethod
    def neither_equality_nor_inequality_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedEquality.equality_not_supported(cls)
        cls = UnsupportedEquality.inequality_not_supported(cls)
        return cls
