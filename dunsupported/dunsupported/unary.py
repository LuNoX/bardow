from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedUnary(UnsupportedOperation):
    @staticmethod
    def negation_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedUnary.unary_operation_not_supported(
            "neg", "-"
        )(cls)

    @staticmethod
    def positive_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedUnary.unary_operation_not_supported(
            "pos", "+"
        )(cls)

    @staticmethod
    def inverse_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedUnary.unary_operation_not_supported(
            "invert", "~"
        )(cls)

    @staticmethod
    def unary_operations_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedUnary.negation_not_supported(cls)
        cls = UnsupportedUnary.positive_not_supported(cls)
        cls = UnsupportedUnary.inverse_not_supported(cls)
        return cls
