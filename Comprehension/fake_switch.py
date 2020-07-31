def get_day_type(day):
    days = {
        (1, 7): 'Fim de semana',
        tuple(range(2, 7)): 'Dia de semana'
    }
    day_selected = (value for key, value in days.items() if day in key)
    return next(day_selected, 'invalid day')


if __name__ == '__main__':
    print(get_day_type(1))

    for day in range(0, 9):
        print(f'{day}: {get_day_type(day)}')
