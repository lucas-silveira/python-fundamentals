# Fibonacci sequence: 0, 1, 1, 2, 3, 5...

def fibonacci(quantity):
    fibonacci_sequence = [0, 1]

    for _ in range(2, quantity):
        fibonacci_sequence.append(sum(fibonacci_sequence[-2:]))

    return fibonacci_sequence


# Lists are mutable and we need be careful
# We can prevent this by using tuples instead lists
def recursive_fibonacci(quantity, sequence=(0, 1)):
    if len(sequence) < quantity:
        sequence = sequence + (sum(sequence[-2:]),)
        return recursive_fibonacci(quantity, sequence)

    return sequence


if __name__ == '__main__':
    print(recursive_fibonacci(10))
