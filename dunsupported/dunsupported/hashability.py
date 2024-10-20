from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedHashability(UnsupportedOperation):
    @staticmethod
    def hashability_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedHashability.unary_operation_not_supported(
                "hash", "hash(obj)", message, error_type
            )(cls)

        return decorator
