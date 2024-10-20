from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedAsync(UnsupportedOperation):
    @staticmethod
    def asynchronous_enter_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedAsync.unary_operation_not_supported(
                "aenter", "async with obj: (entering)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def asynchronous_exit_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedAsync.unary_operation_not_supported(
                "aexit", "async with obj: (exiting)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def asynchronous_iteration_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedAsync.unary_operation_not_supported(
                "aiter", "aiter(obj)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def asynchronous_next_item_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedAsync.unary_operation_not_supported(
                "anext", "anext(obj)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def awaiting_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedAsync.unary_operation_not_supported(
                "await", "await obj", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def context_management_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedAsync.asynchronous_enter_not_supported(
                message, error_type)(cls)
            cls = UnsupportedAsync.asynchronous_exit_not_supported(
                message, error_type)(cls)
            cls = UnsupportedAsync.asynchronous_iteration_not_supported(
                message, error_type)(cls)
            cls = UnsupportedAsync.asynchronous_next_item_not_supported(
                message, error_type)(cls)
            return cls

        return decorator
