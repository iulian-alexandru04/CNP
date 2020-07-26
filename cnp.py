import string


class CNP:
    def __init__(self, cnp):
        if not self.has_cnp_format(cnp):
            raise ValueError

    @staticmethod
    def has_cnp_format(cnp):
        if len(cnp) != 13:
            return False
        for d in cnp:
            if d not in string.digits:
                return False
        return True

