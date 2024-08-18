from dataclasses import dataclass
from typing import Optional

from bardow.backend import variable


@dataclass
class Backend:
    known: variable.KnownBackend
    unknown: variable.UnknownBackend


@dataclass
class PartialBackend(Backend):
    known: Optional[variable.KnownBackend] = None
    unknown: Optional[variable.UnknownBackend] = None

# TODO: add some operation to combine backends?
