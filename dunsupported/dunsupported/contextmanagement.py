from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedContextManagement(UnsupportedOperation):
    @staticmethod
    def enter_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedContextManagement.unary_operation_not_supported(
            "enter", 'with obj: (entering)'
        )(cls)

    @staticmethod
    def exit_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedContextManagement.unary_operation_not_supported(
            "exit", 'with obj: (exiting)'
        )(cls)

    @staticmethod
    def context_management_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedContextManagement.enter_not_supported(cls)
        cls = UnsupportedContextManagement.exit_not_supported(cls)
        return cls
