from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedMath(UnsupportedOperation):

    @staticmethod
    def divmod_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedMath.operation_left_side_not_supported(
                "divmod", "divmod(obj, x)", message, error_type
            )(cls)

            cls = UnsupportedMath.operation_right_side_not_supported(
                "rdivmod", "divmod(x, obj)", message, error_type
            )(cls)
            return cls

        return decorator

    @staticmethod
    def absolute_value_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedMath.unary_operation_not_supported(
                "abs", "abs(obj)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def as_index_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedMath.unary_operation_not_supported(
                "index", "x[obj]", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def rounding_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedMath.unary_operation_not_supported(
                "round", "round(obj)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def truncation_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedMath.unary_operation_not_supported(
                "trunc", "math.trunc(obj)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def flooring_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedMath.unary_operation_not_supported(
                "floor", "math.floor(obj)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def ceiling_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedMath.unary_operation_not_supported(
                "ceil", "math.ceil(obj)", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def loss_of_precision_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedMath.rounding_not_supported(
                message, error_type)(cls)
            cls = UnsupportedMath.truncation_not_supported(
                message, error_type)(cls)
            cls = UnsupportedMath.flooring_not_supported(
                message, error_type)(cls)
            cls = UnsupportedMath.ceiling_not_supported(
                message, error_type)(cls)
            return cls

        return decorator

    @staticmethod
    def math_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedMath.divmod_not_supported(
                message, error_type)(cls)
            cls = UnsupportedMath.absolute_value_not_supported(
                message, error_type)(cls)
            cls = UnsupportedMath.as_index_not_supported(
                message, error_type)(cls)
            cls = UnsupportedMath.loss_of_precision_not_supported(
                message, error_type)(cls)
            return cls

        return decorator
