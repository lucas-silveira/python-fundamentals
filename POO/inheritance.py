# Herança

# superclass
class Car:
    def __init__(self, name):
        self.name = name


# subclass
class Chevete(Car):
    def __init__(self):
        super().__init__('Chevete')


car = Chevete()
print(car.name)  # Chevete


# Herança múltipla

class LivingBeing:
    @property
    def capabilities(self):
        return ('Dormir', 'Comer', 'Beber')


class Human(LivingBeing):
    @property
    def capabilities(self):
        return super().capabilities + ('Raciocinar', 'Falar', 'Andar')


class Spider(LivingBeing):
    @property
    def capabilities(self):
        return super().capabilities + ('Soltar teia', 'Grudar na parede')


class SpiderMan(Human, Spider):
    @property
    def capabilities(self):
        return super().capabilities + ('Super força',)


peter = SpiderMan()

print(peter.capabilities)
# ('Dormir', 'Comer', 'Beber', 'Soltar teia', 'Grudar na parede',
# 'Raciocinar', 'Falar', 'Andar', 'Super força')
