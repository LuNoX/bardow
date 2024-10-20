from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedMemoryview(UnsupportedOperation):
    @staticmethod
    def memoryview_creation_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedMemoryview.unary_operation_not_supported(
            "buffer", "memoryview(obj)"
        )(cls)

    @staticmethod
    def memoryview_deletion_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedMemoryview.unary_operation_not_supported(
            "release_buffer", "del memoryview(obj)"
        )(cls)

    @staticmethod
    def context_management_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedMemoryview.memoryview_creation_not_supported(cls)
        cls = UnsupportedMemoryview.memoryview_deletion_not_supported(cls)
        return cls
