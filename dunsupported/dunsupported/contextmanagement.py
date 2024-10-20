from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedContextManagement(UnsupportedOperation):
    @staticmethod
    def enter_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedContextManagement.unary_operation_not_supported(
                "enter", 'with obj: (entering)', message, error_type
            )(cls)

        return decorator

    @staticmethod
    def exit_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedContextManagement.unary_operation_not_supported(
                "exit", 'with obj: (exiting)', message, error_type
            )(cls)

        return decorator

    @staticmethod
    def context_management_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedContextManagement.enter_not_supported(
                message, error_type)(cls)

        cls = UnsupportedContextManagement.exit_not_supported(
            message, error_type)(cls)
        return cls

    return decorator
