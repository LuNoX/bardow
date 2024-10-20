from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedMetaprogramming(UnsupportedOperation):
    # TODO: add warning that these should only be used with caution
    @staticmethod
    def preparing_class_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedMetaprogramming.unary_operation_not_supported(
                "prepare", f"class {cls.__name__}: ...", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def instance_checking_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedMetaprogramming.unary_operation_not_supported(
                "instancecheck", f"isinstance(x, {cls.__name__})", message,
                error_type
            )(cls)

        return decorator

    @staticmethod
    def subclass_checking_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedMetaprogramming.unary_operation_not_supported(
                "issubclass", f"issubclass(X, {cls.__name__})", message,
                error_type
            )(cls)

        return decorator

    @staticmethod
    def subclassing_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedMetaprogramming.unary_operation_not_supported(
                "init_subclass", f"class X({cls.__name__}): ...", message,
                error_type
            )(cls)

        return decorator

    @staticmethod
    def getting_mro_entries_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedMetaprogramming.unary_operation_not_supported(
                "mro_entries", f"class X({cls.__name__}): ...", message,
                error_type
            )(cls)

        return decorator

    @staticmethod
    def getting_class_item_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedMetaprogramming.unary_operation_not_supported(
                "class_getitem", f"{cls.__name__}[x]", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def metaprogramming_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedMetaprogramming.preparing_class_not_supported(
                message, error_type)(cls)
            cls = UnsupportedMetaprogramming.instance_checking_not_supported(
                message, error_type)(cls)
            cls = UnsupportedMetaprogramming.subclass_checking_not_supported(
                message, error_type)(cls)
            cls = UnsupportedMetaprogramming.subclassing_not_supported(
                message, error_type)(cls)
            cls = UnsupportedMetaprogramming.getting_mro_entries_not_supported(
                message, error_type)(cls)
            cls = UnsupportedMetaprogramming.getting_class_item_not_supported(
                message, error_type)(cls)
            return cls

        return decorator
