from mysql.connector import ProgrammingError
from config import new_connection

sql = 'SELECT * FROM contacts LIMIT %s OFFSET %s'

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (10, 0))
        contacts = cursor.fetchall()
    except ProgrammingError as err:
        print(f'Erro: {err.msg}')
    else:
        for contact in contacts:
            print(f'{contact[2]:2d} - {contact[0]:10s} Telefone: {contact[1]}')
            # contact[2]:2d -> 2 dígitos
            # contact[0]:10s -> 10 caracteres
