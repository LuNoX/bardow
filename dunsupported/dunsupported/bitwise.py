from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedBitwise(UnsupportedOperation):
    @staticmethod
    def bitwise_and_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedBitwise.operation_not_supported(
            "and", "&"
        )(cls)

    @staticmethod
    def bitwise_or_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedBitwise.operation_not_supported(
            "or", "|"
        )(cls)

    @staticmethod
    def bitwise_xor_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedBitwise.operation_not_supported(
            "xor", "^"
        )(cls)

    @staticmethod
    def bitwise_rshift_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedBitwise.operation_not_supported(
            "rshift", ">>"
        )(cls)

    @staticmethod
    def bitwise_lshift_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedBitwise.operation_not_supported(
            "lshift", "<<"
        )(cls)

    @staticmethod
    def bitwise_operations_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedBitwise.bitwise_and_not_supported(cls)
        cls = UnsupportedBitwise.bitwise_or_not_supported(cls)
        cls = UnsupportedBitwise.bitwise_xor_not_supported(cls)
        cls = UnsupportedBitwise.bitwise_rshift_not_supported(cls)
        cls = UnsupportedBitwise.bitwise_lshift_not_supported(cls)
        return cls
