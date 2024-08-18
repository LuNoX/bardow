from abc import ABC, abstractmethod


class UnitBackend(ABC):
    @property
    @abstractmethod
    def dimension(self):
        raise NotImplementedError()
