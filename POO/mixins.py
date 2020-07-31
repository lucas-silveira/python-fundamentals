class HtmlToStringMixin:
    def __str__(self):
        html = super().__str__()\
                      .replace('(', '<strong>(')\
                      .replace(')', ')</strong>')
        return f'<span>{html}</span>'


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Animal:
    def __init__(self, name, pet=True):
        self.name = name
        self.pet = pet

    def __str__(self):
        return self.name + ' (pet)' if self.pet else ''


class PersonHtml(HtmlToStringMixin, Person):
    pass


class AnimalHtml(HtmlToStringMixin, Animal):
    pass


if __name__ == '__main__':
    person = Person('Mary')
    person_html = PersonHtml('Alice')
    animal = Animal('Cachorro')
    animal_html = AnimalHtml('Cachorro')

    print(person)  # Alice
    print(person_html)  # <span>Alice</span>
    print(animal)  # Cachorro (Pet)
    print(animal_html)  # <span>Cachorro <strong>(pet)</strong></span>
