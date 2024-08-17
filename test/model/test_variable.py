from copy import copy

import pytest
import sympy
from sympy.physics.units import kelvin, quantities, meter

from bardow.model import variable


class TestVariable:
    initial_name = "test"

    @staticmethod
    def test_instantiation() -> None:
        with pytest.raises(TypeError):
            variable.Variable(name="test")

    @pytest.fixture(scope="class")
    def instance(self) -> variable.Variable:
        variable.Variable.__abstractmethods__ = set()
        instance = variable.Variable(name=self.initial_name)
        return instance

    def test_fields(self, instance: variable.Variable) -> None:
        assert instance.name == self.initial_name
        assert instance.dimension is None

    @staticmethod
    def test_is_known(instance: variable.Variable) -> None:
        assert instance.is_known is False

    @staticmethod
    def test_formula_representation(instance: variable.Variable) -> None:
        with pytest.raises(NotImplementedError):
            instance.formula_representation()


class TestKnown:
    initial_name = "test"
    initial_unit = kelvin
    initial_value = 273.15
    initial_symbol = "T"
    expected_representation = "273.15*kelvin"

    @pytest.fixture(scope="class")
    def instance(self) -> variable.Known:
        known = variable.Known(
            name=self.initial_name,
            unit=copy(self.initial_unit),
            value=self.initial_value,
            symbol=self.initial_symbol
        )
        return known

    @staticmethod
    def test_instantiation(instance: variable.Known) -> None:
        assert isinstance(instance, variable.Known)

    def test_fields(self, instance: variable.Known) -> None:
        assert instance.name == self.initial_name
        assert instance.unit == self.initial_unit
        assert instance.value == self.initial_value
        assert instance.symbol == self.initial_symbol

    def test_dimension(self, instance: variable.Known) -> None:
        assert instance.dimension == self.initial_unit.dimension

    @staticmethod
    def test_is_known(instance: variable.Known) -> None:
        assert instance.is_known is True

    def test_sympy_quantity(self, instance: variable.Known) -> None:
        quantity = instance._sympy_quantity
        assert isinstance(quantity, quantities.Quantity)
        assert quantity.dimension == self.initial_unit.dimension

    def test_formula_representation(self, instance: variable.Known) -> None:
        assert isinstance(instance.formula_representation(), str)
        assert (instance.formula_representation()
                == self.expected_representation)


class TestUnknown:
    initial_name = "test"
    initial_symbol = "T"
    initial_dimension = kelvin.dimension

    @pytest.fixture(scope="class")
    def instance(self) -> variable.Unknown:
        instance = variable.Unknown(
            name=self.initial_name,
            symbol=self.initial_symbol,
            dimension=copy(self.initial_dimension)
        )
        return instance

    @staticmethod
    def test_instantiation(instance: variable.Unknown) -> None:
        assert isinstance(instance, variable.Unknown)

    @staticmethod
    def test_is_unknown(instance: variable.Unknown) -> None:
        assert instance.is_known is False

    def test_formula_representation(self, instance: variable.Unknown) -> None:
        assert instance.formula_representation() == self.initial_symbol

    @staticmethod
    def test_sympy_symbol(instance: variable.Unknown) -> None:
        assert isinstance(instance._sympy_symbol, sympy.Symbol)

    def test_create_known(self, instance: variable.Unknown) -> None:
        unit = kelvin
        value = 273.15
        expected_known = variable.Known(
            name=self.initial_name,
            unit=unit,
            value=value,
            symbol=self.initial_symbol
        )
        known = instance.create_known(value, unit)

        assert known == expected_known


if __name__ == '__main__':
    pytest.main()
