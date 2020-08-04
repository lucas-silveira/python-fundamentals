from locale import setlocale, LC_ALL
from calendar import mdays, month_name

setlocale(LC_ALL, 'pt_BR.utf8')
print(month_name[1])  # janeiro

# list comprehension (imperative)
months_31 = [month_name[key]
             for key, value in enumerate(mdays) if value == 31]
print(months_31)
# ['janeiro', 'março', 'maio', 'julho', 'agosto', 'outubro', 'dezembro']


# immutability functions (declarative)
months_31 = filter(lambda month: mdays[month] == 31, range(1, 13))
months_name_31 = map(lambda month: month_name[month], months_31)
print(list(months_name_31))
# ['janeiro', 'março', 'maio', 'julho', 'agosto', 'outubro', 'dezembro']
