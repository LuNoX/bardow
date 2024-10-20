from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedDescriptors(UnsupportedOperation):
    # TODO: add docs explaining that these need to be applied to the field
    #  NOT the class as follows:
    #  class T:
    #      x = decorator(y)

    # TODO: change type hint from Type[T] to T as it doesnt take in a class but
    #  an object
    @staticmethod
    def setting_name_descriptor_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedDescriptors.unary_operation_not_supported(
                "set_name", "class T: x = Y()", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def getting_value_descriptor_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedDescriptors.unary_operation_not_supported(
                "get", "obj.x", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def setting_value_descriptor_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedDescriptors.unary_operation_not_supported(
                "set", "obj.x = y", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def deleting_value_descriptor_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedDescriptors.unary_operation_not_supported(
                "del", "del obj.x", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def descriptors_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedDescriptors.setting_name_descriptor_not_supported(
                cls)

        cls = UnsupportedDescriptors.getting_value_descriptor_not_supported(
            cls)
        cls = UnsupportedDescriptors.setting_value_descriptor_not_supported(
            cls)
        cls = UnsupportedDescriptors.deleting_value_descriptor_not_supported(
            cls)
        return cls

    return decorator
