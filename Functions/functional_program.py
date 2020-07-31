def execute(func):
    if callable(func):
        func()


def good_morning():
    print('Bom dia!')


if __name__ == '__main__':
    execute(good_morning)  # Bom dia!
    execute(1)  # nothing
