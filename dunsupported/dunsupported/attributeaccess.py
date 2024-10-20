from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedAttributeAccess(UnsupportedOperation):
    @staticmethod
    def getting_missing_attribute_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedAttributeAccess.unary_operation_not_supported(
            "getattr", "obj.missing_attribute"
        )(cls)

    @staticmethod
    def getting_attribute_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedAttributeAccess.unary_operation_not_supported(
            "getattribute", "obj.x"
        )(cls)

    @staticmethod
    def setting_attribute_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedAttributeAccess.unary_operation_not_supported(
            "setattr", "obj.x = y"
        )(cls)

    @staticmethod
    def deleting_attribute_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedAttributeAccess.unary_operation_not_supported(
            "delattr", "del obj.x"
        )(cls)

    @staticmethod
    def attributes_as_list_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedAttributeAccess.unary_operation_not_supported(
            "dir", "dir(obj)"
        )(cls)

    @staticmethod
    def accessing_attributes_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedAttributeAccess. \
            getting_missing_attribute_not_supported(cls)
        cls = UnsupportedAttributeAccess.getting_attribute_not_supported(cls)
        cls = UnsupportedAttributeAccess.setting_attribute_not_supported(cls)
        cls = UnsupportedAttributeAccess.deleting_attribute_not_supported(cls)
        cls = UnsupportedAttributeAccess.attributes_as_list_not_supported(cls)
        return cls
