from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedCollections(UnsupportedOperation):
    @staticmethod
    def length_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedCollections.unary_operation_not_supported(
                "len", "len(obj)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def iteration_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedCollections.unary_operation_not_supported(
                "iter", "iter(obj)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def getting_item_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedCollections.unary_operation_not_supported(
                "getitem", "obj[x]", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def setting_item_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedCollections.unary_operation_not_supported(
                "setitem", "obj[x] = y", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def deleting_item_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedCollections.unary_operation_not_supported(
                "delitem", "del obj[x]", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def contains_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedCollections.unary_operation_not_supported(
                "contains", "x in obj", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def reversing_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedCollections.unary_operation_not_supported(
                "reversed", "reversed(obj)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def next_item_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedCollections.unary_operation_not_supported(
                "next", "next(obj)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def missing_item_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedCollections.unary_operation_not_supported(
                "missing", "obj[x]", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def length_hinting_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedCollections.unary_operation_not_supported(
                "length_hint", "operator.length_hint(obj)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def context_management_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedCollections.length_not_supported(
                message, error_type)(cls)

        cls = UnsupportedCollections.iteration_not_supported(
            message, error_type)(cls)
        cls = UnsupportedCollections.getting_item_not_supported(
            message, error_type)(cls)
        cls = UnsupportedCollections.setting_item_not_supported(
            message, error_type)(cls)
        cls = UnsupportedCollections.deleting_item_not_supported(
            message, error_type)(cls)
        cls = UnsupportedCollections.contains_not_supported(
            message, error_type)(cls)
        cls = UnsupportedCollections.reversing_not_supported(
            message, error_type)(cls)
        cls = UnsupportedCollections.next_item_not_supported(
            message, error_type)(cls)
        cls = UnsupportedCollections.missing_item_not_supported(
            message, error_type)(cls)
        cls = UnsupportedCollections.length_hinting_not_supported(
            message, error_type)(cls)
        return cls

    return decorator
