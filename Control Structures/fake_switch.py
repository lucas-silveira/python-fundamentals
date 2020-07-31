def get_weekly_day(day):
    days = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado',
    }
    return days.get(day, 'invalid day')


if __name__ == '__main__':
    for day in range(1, 8):
        print(get_weekly_day(day))
