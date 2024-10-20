from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedHashability(UnsupportedOperation):
    @staticmethod
    def hashability_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedHashability.unary_operation_not_supported(
            "hash", "hash(obj)"
        )(cls)
