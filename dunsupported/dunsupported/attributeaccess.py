from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedAttributeAccess(UnsupportedOperation):
    @staticmethod
    def getting_missing_attribute_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedAttributeAccess.unary_operation_not_supported(
                "getattr", "obj.missing_attribute", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def getting_attribute_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedAttributeAccess.unary_operation_not_supported(
                "getattribute", "obj.x", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def setting_attribute_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedAttributeAccess.unary_operation_not_supported(
                "setattr", "obj.x = y", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def deleting_attribute_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedAttributeAccess.unary_operation_not_supported(
                "delattr", "del obj.x", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def attributes_as_list_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedAttributeAccess.unary_operation_not_supported(
                "dir", "dir(obj)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def accessing_attributes_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedAttributeAccess. \
                getting_missing_attribute_not_supported(
                message, error_type)(cls)

            cls = UnsupportedAttributeAccess.getting_attribute_not_supported(
                message, error_type)(cls)

            cls = UnsupportedAttributeAccess.setting_attribute_not_supported(
                message, error_type)(cls)

            cls = UnsupportedAttributeAccess.deleting_attribute_not_supported(
                message, error_type)(cls)

            cls = UnsupportedAttributeAccess.attributes_as_list_not_supported(
                message, error_type)(cls)

            return cls

        return decorator
