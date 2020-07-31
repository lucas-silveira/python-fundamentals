class Power:
    def __init__(self, exponent):
        self.exponent = exponent

    # Este método será chamado quando usarmos o objeto como função
    def __call__(self, base):
        return base ** self.exponent


if __name__ == '__main__':
    power2 = Power(2)
    power3 = Power(3)

    if callable(power2) and callable(power3):
        print(f'3² -> {power2(3)}')  # 3² -> 9
        print(f'3³ -> {power3(3)}')  # 3³ -> 27
        print(Power(4)(2))  # 16
