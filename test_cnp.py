import pytest
from cnp import CNP


class TestCNP:
    def test_cnp_format(self):
        assert not CNP.has_cnp_format('abc')
        assert not CNP.has_cnp_format('1234')
        assert CNP.has_cnp_format('1234567890123')
    
    def test_valid_init(self):
        CNP('2234567890123')

    def test_invalid_init(self):
        with pytest.raises(ValueError):
            CNP('abcxy')

