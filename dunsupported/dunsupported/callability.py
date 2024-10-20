from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedCallability(UnsupportedOperation):
    @staticmethod
    def callability_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedCallability.unary_operation_not_supported(
            "call", "obj()"
        )(cls)
