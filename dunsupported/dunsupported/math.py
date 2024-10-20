from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedMath(UnsupportedOperation):

    @staticmethod
    def divmod_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedMath.operation_left_side_not_supported(
            "divmod", "divmod(obj, x)"
        )(cls)
        cls = UnsupportedMath.operation_right_side_not_supported(
            "rdivmod", "divmod(x, obj)"
        )(cls)
        return cls

    @staticmethod
    def absolute_value_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedMath.unary_operation_not_supported(
            "abs", "abs(obj)"
        )(cls)

    @staticmethod
    def as_index_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedMath.unary_operation_not_supported(
            "index", "x[obj]"
        )(cls)

    @staticmethod
    def rounding_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedMath.unary_operation_not_supported(
            "round", "round(obj)"
        )(cls)

    @staticmethod
    def truncation_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedMath.unary_operation_not_supported(
            "trunc", "math.trunc(obj)"
        )(cls)

    @staticmethod
    def flooring_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedMath.unary_operation_not_supported(
            "floor", "math.floor(obj)"
        )(cls)

    @staticmethod
    def ceiling_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedMath.unary_operation_not_supported(
            "ceil", "math.ceil(obj)"
        )(cls)

    @staticmethod
    def loss_of_precision_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedMath.rounding_not_supported(cls)
        cls = UnsupportedMath.truncation_not_supported(cls)
        cls = UnsupportedMath.flooring_not_supported(cls)
        cls = UnsupportedMath.ceiling_not_supported(cls)
        return cls

    @staticmethod
    def math_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedMath.divmod_not_supported(cls)
        cls = UnsupportedMath.absolute_value_not_supported(cls)
        cls = UnsupportedMath.as_index_not_supported(cls)
        cls = UnsupportedMath.loss_of_precision_not_supported(cls)
        return cls
