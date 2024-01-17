from dataclasses import dataclass


@dataclass
class Unit:
    name: str
    symbol: str

    _converter: Converter = Converter.converter()

    def register_conversion(self, factor: float, to_unit: 'Unit') -> None:
        self._converter.register_conversion(self, factor, to_unit)

    def convert_to(self, to_unit: 'Unit') -> float:
        return Converter.covert_from_to(self, to_unit)

  
class Converter:
    _converter: 'Converter' = None
    _conversion = {}

    @classmethod
    def converter(cls) -> 'Converter':
        if cls._converter is None:
            cls._converter = Converter()
        return cls._converter

    @classmethod
    def register_conversion(cls, from_unit: Unit, factor: float,
                            to_unit: Unit) -> None:
        ...

    @classmethod
    def covert_from_to(cls, from_unit: Unit, to_unit: Unit) -> float:
        ...
