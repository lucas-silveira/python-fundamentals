def sum_2(a, b):
    return a + b


def sum_3(a, b, c):
    return a + b + c


# packing
def sum_n(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total


# named packing (dict)
def get_cart(**products):
    total = 0
    for key, value in products.items():
        total += value
        print(f'{key} -> R$ {value}')
    print(f'Total: R$ {total}')


def get_cart2(product1, product2):
    print(f'1) {product1}')
    print(f'2) {product2}')


# getting all args
def get_all_args(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == "__main__":
    print(sum_2(2, 3))  # 5
    print(sum_3(2, 3, 4))  # 9
    print(sum_n(2, 3, 4, 5, 6))  # 20

    # unpacking
    tupla_numbers = (1, 2, 3)
    print(sum_n(*tupla_numbers))  # 6
    list_numbers = [3, 4, 5]
    set_numbers = [3, 4, 5]
    print(sum_n(*list_numbers))  # 12

    get_cart(Iphone=2000, Macbook=2200)
    # Iphone -> R$ 2000
    # Macbook -> R$ 2200

    # named unpacking
    products = {'product1': 'Iphone', 'product2': 'Macbook'}
    get_cart2(**products)
    # 1) Iphone
    # 2) Macbook

    get_all_args('a', 'b', 'c')
    # args: ('a', 'b', 'c')
    # kwargs: {}
    get_all_args('a', 'b', 'c', ok=True)
    # args: ('a', 'b', 'c')
    # kwargs: {'ok': True}

    # get_all_args(ok=True, 'a')  # error
