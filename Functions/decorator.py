def log(function):
    def decorator(*args, **kwargs):
        print(f'Início da chamada da função: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        result = function(*args, **kwargs)
        print(f'Resultado da chamada: {result}')
        return result

    return decorator


@log
def sum(x, y):
    return x + y


@log
def sub(x, y):
    return x - y


if __name__ == '__main__':
    sum(2, 3)
    sub(3, 2)
