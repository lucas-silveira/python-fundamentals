from mysql.connector import ProgrammingError
from config import new_connection

sql = 'SELECT * FROM contacts WHERE name LIKE %s'

with new_connection() as connection:
    try:
        name = input('Contato a localizar: ')
        cursor = connection.cursor()
        args = (f'%{name}%',)
        cursor.execute(sql, args)
    except ProgrammingError as err:
        print(f'Erro: {err.msg}')
    else:
        print(cursor.fetchone())
