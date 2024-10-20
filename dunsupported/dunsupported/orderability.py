from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedOrderability(UnsupportedOperation):
    @staticmethod
    def less_than_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedOrderability.operation_not_supported(
            "lt", "<"
        )(cls)

    @staticmethod
    def less_than_equal_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedOrderability.operation_not_supported(
            "le", "<="
        )(cls)

    @staticmethod
    def greater_than_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedOrderability.operation_not_supported(
            "lt", ">"
        )(cls)

    @staticmethod
    def greater_than_equal_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedOrderability.operation_not_supported(
            "le", ">="
        )(cls)

    @staticmethod
    def orderability_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedOrderability.less_than_not_supported(cls)
        cls = UnsupportedOrderability.less_than_equal_not_supported(cls)
        cls = UnsupportedOrderability.greater_than_not_supported(cls)
        cls = UnsupportedOrderability.greater_than_equal_not_supported(cls)
        return cls
