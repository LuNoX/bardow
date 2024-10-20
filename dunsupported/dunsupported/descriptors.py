from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedDescriptors(UnsupportedOperation):
    # TODO: add docs explaining that these need to be applied to the field
    #  NOT the class as follows:
    #  class T:
    #      x = decorator(y)

    # TODO: change type hint from Type[T] to T as it doesnt take in a class but
    #  an object
    @staticmethod
    def setting_name_descriptor_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedDescriptors.unary_operation_not_supported(
            "set_name", "class T: x = Y()"
        )(cls)

    @staticmethod
    def getting_value_descriptor_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedDescriptors.unary_operation_not_supported(
            "get", "obj.x"
        )(cls)

    @staticmethod
    def setting_value_descriptor_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedDescriptors.unary_operation_not_supported(
            "set", "obj.x = y"
        )(cls)

    @staticmethod
    def deleting_value_descriptor_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedDescriptors.unary_operation_not_supported(
            "del", "del obj.x"
        )(cls)

    @staticmethod
    def descriptors_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedDescriptors.setting_name_descriptor_not_supported(cls)
        cls = UnsupportedDescriptors.getting_value_descriptor_not_supported(
            cls)
        cls = UnsupportedDescriptors.setting_value_descriptor_not_supported(
            cls)
        cls = UnsupportedDescriptors.deleting_value_descriptor_not_supported(
            cls)
        return cls
