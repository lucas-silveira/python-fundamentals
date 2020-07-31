import math
import re


COLOR_ERROR = '\033[91m'
COLOR_DEFAULT = '\033[0m'


def get_circle_area(radius):
    return math.pi * float(radius) ** 2


radius = input('Informe o raio: ')  # get value through input terminal
if re.search('[A-Za-z]', radius):
    print(COLOR_ERROR + 'O raio deve ser um valor numérico' + COLOR_DEFAULT)
    exit()
area = get_circle_area(radius)
print('Área do círculo', area)
