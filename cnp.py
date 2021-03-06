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
        county_idx = self.__get_county_index()
        if county_idx < 1 or county_idx > 52:
            raise ValueError('invalid county code')
        if cnp[9:12] == '000':
            raise ValueError
        if int(cnp[-1]) != self.__compute_control():
            raise ValueError

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

    def __get_county_index(self):
        return int(self.__cnp[7:9])

    @property
    def county(self):
        return counties[self.__get_county_index() - 1]

    @staticmethod
    def has_cnp_format(cnp):
        if len(cnp) != 13:
            return False
        for d in cnp:
            if d not in string.digits:
                return False
        return True

    def __compute_control(self):
        total = sum(int(x) * int(y) for x, y in zip(self.__cnp, '279146358279'))
        control = total % 11
        return 1 if control == 10 else control

counties = ['Alba', 'Arad', 'Argeș', 'Bacău', 'Bihor', 'Bistrița-Năsăud', 'Botoșani', 'Brașov', 
            'Brăila', 'Buzău', 'Caraș-Severin', 'Cluj', 'Constanța', 'Covasna', 'Dâmbovița', 
            'Dolj', 'Galați', 'Gorj', 'Harghita', 'Hunedoara', 'Ialomița', 'Iași', 'Ilfov', 
            'Maramureș', 'Mehedinți', 'Mureș', 'Neamț', 'Olt', 'Prahova', 'Satu Mare', 'Sălaj', 
            'Sibiu', 'Suceava', 'Teleorman', 'Timiș', 'Tulcea', 'Vaslui', 'Vâlcea', 'Vrancea', 
            'București', 'București Sector 1', 'București Sector 2', 'București Sector 3', 
            'București Sector 4', 'București Sector 5', 'București Sector 6', 'Călărași', 'Giurgiu']
