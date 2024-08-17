import pytest

from bardow.model import errors


class TestErrors:
    @staticmethod
    def test_cannot_convert_error() -> None:
        with pytest.raises(errors.CannotConvertError):
            raise errors.CannotConvertError("This is a test error")

    @staticmethod
    def test_not_solvable_error() -> None:
        with pytest.raises(errors.NotSolvableError):
            raise errors.NotSolvableError("This is a test error")

    @staticmethod
    def test_too_few_knowns_error() -> None:
        with pytest.raises(errors.TooFewKnownsError):
            raise errors.TooFewKnownsError("This is a test error")


if __name__ == '__main__':
    pytest.main()
