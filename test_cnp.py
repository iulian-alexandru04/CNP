from cnp import CNP


class TestCNP:
    def test_cnp_format(self):
        assert not CNP.has_cnp_format('abc')
        assert not CNP.has_cnp_format('1234')
        assert CNP.has_cnp_format('1234567890123')

