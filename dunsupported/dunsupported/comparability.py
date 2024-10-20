from typing import Type, Callable

from dunsupported.dunsupported.equality import UnsupportedEquality
from dunsupported.dunsupported.operation import T
from dunsupported.dunsupported.orderability import UnsupportedOrderability


class UnsupportedComparison(UnsupportedEquality, UnsupportedOrderability):
    @staticmethod
    def comparison_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedComparison. \
                neither_equality_nor_inequality_supported(
                message, error_type)(cls)
            cls = UnsupportedComparison.orderability_not_supported(
                message, error_type)(cls)
            return cls

        return decorator
