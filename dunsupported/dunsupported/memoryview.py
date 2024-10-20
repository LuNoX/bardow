from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedMemoryview(UnsupportedOperation):
    @staticmethod
    def memoryview_creation_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedMemoryview.unary_operation_not_supported(
                "buffer", "memoryview(obj)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def memoryview_deletion_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedMemoryview.unary_operation_not_supported(
                "release_buffer", "del memoryview(obj)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def context_management_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedMemoryview.memoryview_creation_not_supported(
                message, error_type)(cls)
            cls = UnsupportedMemoryview.memoryview_deletion_not_supported(
                message, error_type)(cls)
            return cls

        return decorator
