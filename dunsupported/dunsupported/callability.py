from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedCallability(UnsupportedOperation):
    @staticmethod
    def callability_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedCallability.unary_operation_not_supported(
                "call", "obj()", message, error_type
            )(cls)

        return decorator
