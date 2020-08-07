from mysql.connector import ProgrammingError
from config import new_connection

sql = 'SELECT name, phone FROM contacts LIMIT %s OFFSET %s'

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (10, 0))
        contacts = cursor.fetchall()
    except ProgrammingError as err:
        print(f'Erro: {err.msg}')
    else:
        for contact in contacts:
            print('\t'.join(str(field) for field in contact))
