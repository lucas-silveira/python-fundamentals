from os import path
import csv

with open(path.join(path.dirname(__file__), 'persons.csv')) as input_file:
    for person in csv.reader(input_file):
        print('Nome: {}, Idade: {}'.format(*person))
