from bardow.backend import backend
from bardow.backend.implementations import sympy

DEFAULT_BACKEND = sympy.SYMPY_BACKEND


def switch_default_backend(new_default: backend.Backend) -> None:
    global DEFAULT_BACKEND
    DEFAULT_BACKEND = new_default
