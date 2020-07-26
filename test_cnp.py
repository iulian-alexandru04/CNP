import pytest
from cnp import CNP, Gender


class TestCNP:
    def test_cnp_format(self):
        assert not CNP.has_cnp_format('abc')
        assert not CNP.has_cnp_format('1234')
        assert CNP.has_cnp_format('1234567890123')

    def test_valid_init(self):
        CNP('2230427890123')

    def test_invalid_init(self):
        with pytest.raises(ValueError):
            CNP('abcxy')

    def test_gender(self):
        assert CNP('1230517890123').gender == Gender.MALE
        assert CNP('3230517890123').gender == Gender.MALE
        assert CNP('5230517890123').gender == Gender.MALE
        assert CNP('7230517890123').gender == Gender.MALE
        assert CNP('2230517890123').gender == Gender.FEMALE
        assert CNP('4230517890123').gender == Gender.FEMALE
        assert CNP('6230517890123').gender == Gender.FEMALE
        assert CNP('8230517890123').gender == Gender.FEMALE
        assert CNP('9230517890123').gender == Gender.UNKNOWN

    def test_century(self):
        assert CNP('1230807890123').century == 20
        assert CNP('2230807890123').century == 20
        assert CNP('3230807890123').century == 19
        assert CNP('4230807890123').century == 19
        assert CNP('5230807890123').century == 21
        assert CNP('6230807890123').century == 21
        assert CNP('7230807890123').century == 20
        assert CNP('8230807890123').century == 20
        assert CNP('9230807890123').century == 20

    def test_year(self):
        assert CNP('7711105890123').year == 1971

    def test_month(self):
        assert CNP('1230517890123').month == 5

    def test_day(self):
        assert CNP('1230520890123').day == 20

    def test_invalid_month(self):
        with pytest.raises(ValueError):
            CNP('1231520890123')

    def test_invalid_day_over_31(self):
        with pytest.raises(ValueError):
            CNP('2931133890123')

    def test_day_31_for_months_with_less(self):
        with pytest.raises(ValueError):
            CNP('5030231000123')
        with pytest.raises(ValueError):
            CNP('5030431000123')
        with pytest.raises(ValueError):
            CNP('5030631000123')
        with pytest.raises(ValueError):
            CNP('5030931000123')
        with pytest.raises(ValueError):
            CNP('5031131000123')

    def test_day_30_for_february(self):
        with pytest.raises(ValueError):
            CNP('5030230000123')
        with pytest.raises(ValueError):
            CNP('6020230000123')
        with pytest.raises(ValueError):
            CNP('9020230000123')

    def test_29_february_for_non_leap_years(self):
        with pytest.raises(ValueError):
            CNP('1030229000123')
        with pytest.raises(ValueError):
            CNP('2000229000123')

    def test_29_february_for_leap_yars(self):
            CNP('3040229000123')
            CNP('6000229000123')

