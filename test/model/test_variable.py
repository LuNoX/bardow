import unittest
from unittest.mock import patch

from bardow.model import variable


class TestVariable(unittest.TestCase):

    def test_instantiation(self) -> None:
        with self.assertRaises(TypeError):
            variable.Variable(name="test")

    @patch.multiple(variable.Variable, __abstractmethods__=set())
    def test_fields(self) -> None:
        name = "test"
        self.instance = variable.Variable(name=name)
        self.assertEqual(self.instance.name, name)
        self.assertIs(self.instance.dimension, None)


class TestKnown(unittest.TestCase):
    # TODO: implement
    def test_instantiation(self) -> None:
        ...


class TestUnknown(unittest.TestCase):
    # TODO: implement
    def test_instantiation(self) -> None:
        ...


if __name__ == '__main__':
    unittest.main()
