# Class names must be of type CamelCase
class Date:
    def to_str(self):
        return f'{self.day}/{self.monthly}/{self.year}'


d1 = Date()
d1.day = 5  # Em Python podemos atribuir membros à uma classe de forma dinâmica
d1.monthly = 5
d1.year = 2020
print(d1.to_str())  # 5/5/2020


class Date2:
    def __init__(self, day, monthly, year):
        self.day = day
        self.monthly = monthly
        self.year = year

    def to_str(self):
        return f'{self.day}/{self.monthly}/{self.year}'


d2 = Date2(7, 5, 2020)
print(d2.to_str())  # 7/5/2020


class Date3:
    def __init__(self, day=1, monthly=1, year=1970):
        self.day = day
        self.monthly = monthly
        self.year = year

    def to_str(self):
        return f'{self.day}/{self.monthly}/{self.year}'

    # This is a special method that returns data of type string when
    # we calling the instance of that class
    def __str__(self):
        return f'{self.day}/{self.monthly}/{self.year}'


# named params
d3 = Date3(day=2)
d3.monthly = 2
print(d3.to_str())  # 2/2/1970
print(d3)  # 2/2/1970


# isinstance

print(isinstance(d3, Date3))  # True
