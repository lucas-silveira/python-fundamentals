# A função calcule tem acesso ao x que está fora do seu escopo pois ela
# está dentro do contexto de x.

def multiply(x):
    def calcule(y):
        return x * y
    return calcule


if __name__ == '__main__':
    double = multiply(2)
    triple = multiply(3)

    print(double(3))  # 6
    print(triple(3))  # 9
