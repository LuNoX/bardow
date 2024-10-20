from typing import Type

from dunsupported.dunsupported.equality import UnsupportedEquality
from dunsupported.dunsupported.operation import T
from dunsupported.dunsupported.orderability import UnsupportedOrderability


class UnsupportedComparison(UnsupportedEquality, UnsupportedOrderability):
    @staticmethod
    def comparison_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedComparison. \
            neither_equality_nor_inequality_supported(cls)
        cls = UnsupportedComparison.orderability_not_supported(cls)
        return cls
