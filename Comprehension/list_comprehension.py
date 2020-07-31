# [statement for item in list if conditional]

doubles = [i * 2 for i in range(10)]
doubles_of_evens = [i * 2 for i in range(10) if i % 2 == 0]


if __name__ == '__main__':
    print(doubles)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    print(doubles_of_evens)  # [0, 4, 8, 12, 16]
