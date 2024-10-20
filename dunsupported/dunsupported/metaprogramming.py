from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedMetaprogramming(UnsupportedOperation):
    # TODO: add warning that these should only be used with caution
    @staticmethod
    def preparing_class_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedMetaprogramming.unary_operation_not_supported(
            "prepare", f"class {cls.__name__}: ..."
        )(cls)

    @staticmethod
    def instance_checking_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedMetaprogramming.unary_operation_not_supported(
            "instancecheck", f"isinstance(x, {cls.__name__})"
        )(cls)

    @staticmethod
    def subclass_checking_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedMetaprogramming.unary_operation_not_supported(
            "issubclass", f"issubclass(X, {cls.__name__})"
        )(cls)

    @staticmethod
    def subclassing_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedMetaprogramming.unary_operation_not_supported(
            "init_subclass", f"class X({cls.__name__}): ..."
        )(cls)

    @staticmethod
    def getting_mro_entries_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedMetaprogramming.unary_operation_not_supported(
            "mro_entries", f"class X({cls.__name__}): ..."
        )(cls)

    @staticmethod
    def getting_class_item_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedMetaprogramming.unary_operation_not_supported(
            "class_getitem", f"{cls.__name__}[x]"
        )(cls)

    @staticmethod
    def metaprogramming_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedMetaprogramming.preparing_class_not_supported(cls)
        cls = UnsupportedMetaprogramming.instance_checking_not_supported(cls)
        cls = UnsupportedMetaprogramming.subclass_checking_not_supported(cls)
        cls = UnsupportedMetaprogramming.subclassing_not_supported(cls)
        cls = UnsupportedMetaprogramming.getting_mro_entries_not_supported(cls)
        cls = UnsupportedMetaprogramming.getting_class_item_not_supported(cls)
        return cls
