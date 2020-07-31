for x in range(10):
    if x % 2 == 0:
        continue  # interrompe a iteração e vai para a próxima
    print(x, end=', ')
print()

for x in range(10):
    if x == 5:
        break  # finaliza o laço
    print(x, end=', ')
print()
