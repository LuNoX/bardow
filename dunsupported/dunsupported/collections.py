from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedCollections(UnsupportedOperation):
    @staticmethod
    def length_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedCollections.unary_operation_not_supported(
            "len", "len(obj)"
        )(cls)

    @staticmethod
    def iteration_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedCollections.unary_operation_not_supported(
            "iter", "iter(obj)"
        )(cls)

    @staticmethod
    def getting_item_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedCollections.unary_operation_not_supported(
            "getitem", "obj[x]"
        )(cls)

    @staticmethod
    def setting_item_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedCollections.unary_operation_not_supported(
            "setitem", "obj[x] = y"
        )(cls)

    @staticmethod
    def deleting_item_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedCollections.unary_operation_not_supported(
            "delitem", "del obj[x]"
        )(cls)

    @staticmethod
    def contains_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedCollections.unary_operation_not_supported(
            "contains", "x in obj"
        )(cls)

    @staticmethod
    def reversing_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedCollections.unary_operation_not_supported(
            "reversed", "reversed(obj)"
        )(cls)

    @staticmethod
    def next_item_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedCollections.unary_operation_not_supported(
            "next", "next(obj)"
        )(cls)

    @staticmethod
    def missing_item_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedCollections.unary_operation_not_supported(
            "missing", "obj[x]"
        )(cls)

    @staticmethod
    def length_hinting_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedCollections.unary_operation_not_supported(
            "length_hint", "operator.length_hint(obj)"
        )(cls)

    @staticmethod
    def context_management_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedCollections.length_not_supported(cls)
        cls = UnsupportedCollections.iteration_not_supported(cls)
        cls = UnsupportedCollections.getting_item_not_supported(cls)
        cls = UnsupportedCollections.setting_item_not_supported(cls)
        cls = UnsupportedCollections.deleting_item_not_supported(cls)
        cls = UnsupportedCollections.contains_not_supported(cls)
        cls = UnsupportedCollections.reversing_not_supported(cls)
        cls = UnsupportedCollections.next_item_not_supported(cls)
        cls = UnsupportedCollections.missing_item_not_supported(cls)
        cls = UnsupportedCollections.length_hinting_not_supported(cls)
        return cls
