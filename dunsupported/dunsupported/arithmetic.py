from typing import Type

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedArithmetic(UnsupportedOperation):
    @staticmethod
    def addition_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedArithmetic.operation_not_supported(
            "add", "+"
        )(cls)

    @staticmethod
    def subtraction_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedArithmetic.operation_not_supported(
            "sub", "-"
        )(cls)

    @staticmethod
    def multiplication_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedArithmetic.operation_not_supported(
            "mul", "*"
        )(cls)

    @staticmethod
    def exponentiation_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedArithmetic.operation_not_supported(
            "pow", "**"
        )(cls)

    @staticmethod
    def truedivision_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedArithmetic.operation_not_supported(
            "truediv", "/"
        )(cls)

    @staticmethod
    def floordivision_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedArithmetic.operation_not_supported(
            "floordiv", "//"
        )(cls)

    @staticmethod
    def modulo_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedArithmetic.operation_not_supported(
            "mod", "%"
        )(cls)

    @staticmethod
    def division_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedArithmetic.truedivision_not_supported(cls)
        cls = UnsupportedArithmetic.floordivision_not_supported(cls)
        cls = UnsupportedArithmetic.modulo_not_supported(cls)
        return cls

    @staticmethod
    def matrix_multiplication_not_supported(cls: Type[T]) -> Type[T]:
        return UnsupportedArithmetic.operation_not_supported(
            "matmul", "@"
        )(cls)

    @staticmethod
    def neither_addition_nor_subtraction_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedArithmetic.addition_not_supported(cls)
        cls = UnsupportedArithmetic.subtraction_not_supported(cls)
        return cls

    @staticmethod
    def neither_multiplication_nor_division_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedArithmetic.multiplication_not_supported(cls)
        cls = UnsupportedArithmetic.division_not_supported(cls)
        return cls

    @staticmethod
    def arithmetic_not_supported(cls: Type[T]) -> Type[T]:
        cls = UnsupportedArithmetic. \
            neither_addition_nor_subtraction_supported(cls)
        cls = UnsupportedArithmetic. \
            neither_multiplication_nor_division_supported(cls)
        cls = UnsupportedArithmetic.exponentiation_not_supported(cls)
        cls = UnsupportedArithmetic.matrix_multiplication_not_supported(cls)
        return cls
