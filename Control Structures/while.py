from random import randint

# number = 0
# while number < 10:
#     print(number)
#     number += 1

input_number = int(input('Digite um número: '))
secret_number = randint(0, 9)

while input_number != secret_number:
    input_number = int(input('Errou! Digite um número novamente: '))

print(f'O número secreto {secret_number} foi encontrado!')
