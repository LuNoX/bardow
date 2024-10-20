from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedAsync(UnsupportedOperation):
    @staticmethod
    def asynchronous_enter_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedAsync.unary_operation_not_supported(
            "aenter", 'async with obj: (entering)'
        )(cls)

    @staticmethod
    def asynchronous_exit_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedAsync.unary_operation_not_supported(
            "aexit", 'async with obj: (exiting)'
        )(cls)

    @staticmethod
    def asynchronous_iteration_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedAsync.unary_operation_not_supported(
            "aiter", 'aiter(obj)'
        )(cls)

    @staticmethod
    def asynchronous_next_item_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedAsync.unary_operation_not_supported(
            "anext", 'anext(obj)'
        )(cls)

    @staticmethod
    def awaiting_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedAsync.unary_operation_not_supported(
            "await", 'await obj'
        )(cls)

    @staticmethod
    def context_management_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedAsync.asynchronous_enter_not_supported(cls)
        cls = UnsupportedAsync.asynchronous_exit_not_supported(cls)
        cls = UnsupportedAsync.asynchronous_iteration_not_supported(cls)
        cls = UnsupportedAsync.asynchronous_next_item_not_supported(cls)
        return cls
