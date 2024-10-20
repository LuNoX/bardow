from typing import Type, Callable

from dunsupported.dunsupported.operation import UnsupportedOperation, T


class UnsupportedArithmetic(UnsupportedOperation):
    @staticmethod
    def addition_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedArithmetic.operation_not_supported(
                "add", "+", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def subtraction_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedArithmetic.operation_not_supported(
                "sub", "-", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def multiplication_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedArithmetic.operation_not_supported(
                "mul", "*", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def exponentiation_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedArithmetic.operation_not_supported(
                "pow", "**", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def truedivision_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedArithmetic.operation_not_supported(
                "truediv", "/", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def floordivision_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedArithmetic.operation_not_supported(
                "floordiv", "//", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def modulo_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedArithmetic.operation_not_supported(
                "mod", "%", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def division_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedArithmetic.truedivision_not_supported(
                message, error_type)(cls)
            cls = UnsupportedArithmetic.floordivision_not_supported(
                message, error_type)(cls)
            cls = UnsupportedArithmetic.modulo_not_supported(
                message, error_type)(cls)
            return cls

        return decorator

    @staticmethod
    def matrix_multiplication_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            return UnsupportedArithmetic.operation_not_supported(
                "matmul", "@", message, error_type
            )(cls)

        return decorator

    @staticmethod
    def neither_addition_nor_subtraction_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedArithmetic.addition_not_supported(
                message, error_type)(cls)
            cls = UnsupportedArithmetic.subtraction_not_supported(
                message, error_type)(cls)
            return cls

        return decorator

    @staticmethod
    def neither_multiplication_nor_division_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedArithmetic.multiplication_not_supported(
                message, error_type)(cls)
            cls = UnsupportedArithmetic.division_not_supported(
                message, error_type)(cls)
            return cls

        return decorator

    @staticmethod
    def arithmetic_not_supported(
            message: str = None,
            error_type: Type[Exception] | Callable[[str], Exception] = None
    ) -> Callable[[Type[T]], Type[T]]:
        def decorator(cls: Type[T]) -> Type[T]:
            cls = UnsupportedArithmetic. \
                neither_addition_nor_subtraction_supported(message,
                                                           error_type)(cls)
            cls = UnsupportedArithmetic. \
                neither_multiplication_nor_division_supported(message,
                                                              error_type)(cls)
            cls = UnsupportedArithmetic.exponentiation_not_supported(
                message, error_type)(cls)
            cls = UnsupportedArithmetic.matrix_multiplication_not_supported(
                message, error_type)(cls)
            return cls

        return decorator
