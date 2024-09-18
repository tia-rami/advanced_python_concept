# WRITE YOUR SOLUTION HERE:
class Recording:
    def __init__(self, length: int):
        if length < 0:
            raise ValueError("The length must not be bellow zero")
        self.__length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, given_length: int):
        if given_length < 0:
            raise ValueError("The length must not be bellow zero")
        self.__length = given_length



