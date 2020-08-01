# Em Python lambdas são como funções anônimas.

purchase = (
    {'quantity': 2, 'price': 10},
    {'quantity': 3, 'price': 20},
    {'quantity': 5, 'price': 30},
)


# traditional method
def calc_price_total(purch): return purch['quantity'] * purch['price']


totals = tuple(map(calc_price_total, purchase))

# with lambda
totals_lambda = tuple(
    map(lambda purch: purch['quantity'] * purch['price'], purchase))

print(totals_lambda)  # (20, 60, 150)
print(sum(totals_lambda))  # 230
