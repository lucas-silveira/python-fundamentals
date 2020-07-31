from abc import ABCMeta, abstractproperty


# method 1
class Human:
    @property
    def smart(self):
        raise NotImplementedError('Propriedade não implementada')


class HomoSapiens(Human):
    @property
    def smart(self):
        return True


human = Human()
modern_man = HomoSapiens()

try:
    # print(human.smart)  # error
    print(modern_man.smart)
except NotImplementedError as error:
    print(str(error))


# method 2
class Human2(metaclass=ABCMeta):
    @abstractproperty
    def smart(self):
        pass


class HomoSapiens2(Human2):
    @property
    def smart(self):
        return True


# human = Human2()  # error
modern_man2 = HomoSapiens2()

try:
    print(modern_man2.smart)
except NotImplementedError as error:
    print(str(error))
