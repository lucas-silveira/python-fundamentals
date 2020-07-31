class Human:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError('A idade deve ser um número positivo')

        self._age = age


human = Human(20)
human.age = -10

print(human.age)
