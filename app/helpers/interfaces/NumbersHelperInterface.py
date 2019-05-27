
from interface import Interface

class NumbersHelperInterface(Interface):

    def is_number(self, value) -> bool:
        """
        Check if a given value is a number
        :param value:
        :return: bool true if number, false otherwose
        """
        pass
