import pytest
from cnp import CNP, Gender


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

    def test_gender(self):
        assert CNP('1234567890123').gender == Gender.MALE
        assert CNP('3234567890123').gender == Gender.MALE
        assert CNP('5234567890123').gender == Gender.MALE
        assert CNP('7234567890123').gender == Gender.MALE
        assert CNP('2234567890123').gender == Gender.FEMALE
        assert CNP('4234567890123').gender == Gender.FEMALE
        assert CNP('6234567890123').gender == Gender.FEMALE
        assert CNP('8234567890123').gender == Gender.FEMALE
        assert CNP('9234567890123').gender == Gender.UNKNOWN

    def test_century(self):
        assert CNP('1234567890123').century == 20
        assert CNP('2234567890123').century == 20
        assert CNP('3234567890123').century == 19
        assert CNP('4234567890123').century == 19
        assert CNP('5234567890123').century == 21
        assert CNP('6234567890123').century == 21
        assert CNP('7234567890123').century == 20
        assert CNP('8234567890123').century == 20
        assert CNP('9234567890123').century == 20

    def test_year(self):
        assert CNP('7714567890123').year == 1971

