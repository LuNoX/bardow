from bardow.backend import backendtypes
from bardow.backend.implementations import sympy

DEFAULT_BACKEND = sympy.SYMPY_BACKEND


def switch_default_backend(new_default: backendtypes.BackendTypes) -> None:
    global DEFAULT_BACKEND
    DEFAULT_BACKEND = new_default
