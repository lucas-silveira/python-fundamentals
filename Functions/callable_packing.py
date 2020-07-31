def get_total_price(price, get_tax, *params):
    return price + price * get_tax(*params)


def get_tax(isImported):
    return 0.22 if isImported else 0.13


# named packing
def get_total_price2(price, get_tax, **params):
    return price + price * get_tax(**params)


if __name__ == '__main__':
    price = 2200.90
    total_price = get_total_price(price, get_tax, True)
    print(f'Total: R$ {total_price}')  # 2685.098

    total_price = get_total_price2(price, get_tax, isImported=True)
    print(f'Total: R$ {total_price}')  # 2685.098
