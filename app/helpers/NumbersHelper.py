
class NumbersHelper(object):

    def is_number(self, value) -> bool:
        """
        Check if a given value is a number
        :param value:
        :return: bool true if number, false otherwose
        """
        try:
           # If a value can be converted to a float, then it's a number
           if float(value):
               return True
        except:
            pass
        return False
