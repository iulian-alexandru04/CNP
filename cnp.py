from enum import Enum, unique
from datetime import date
import string


@unique
class Gender(Enum):
    MALE = 1
    FEMALE = 2
    UNKNOWN = 3


class CNP:
    def __init__(self, cnp):
        if not self.has_cnp_format(cnp):
            raise ValueError('wrong format')
        self.__cnp = cnp
        if date.today() < date(self.year, self.month, self.day):
            raise ValueError('birth date is in the future')

    @property
    def gender(self):
        if self.__cnp[0] == '9':
            return Gender.UNKNOWN
        if int(self.__cnp[0]) % 2 == 1:
            return Gender.MALE
        return Gender.FEMALE

    @property
    def century(self):
        if self.__cnp[0] in '34':
            return 19
        if self.__cnp[0] in '56':
            return 21
        return 20

    @property
    def year(self):
        return (self.century - 1) * 100 + int(self.__cnp[1:3])

    @property
    def month(self):
        return int(self.__cnp[3:5])

    @property
    def day(self):
        return int(self.__cnp[5:7])

    @staticmethod
    def has_cnp_format(cnp):
        if len(cnp) != 13:
            return False
        for d in cnp:
            if d not in string.digits:
                return False
        return True

