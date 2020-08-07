from mysql.connector import ProgrammingError
from config import new_connection

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute('SHOW TABLES')

        for i, table in enumerate(cursor, start=1):
            print(f'Tabela {i}: {table[0]}')
    except ProgrammingError as err:
        print(f'Erro: {err.msg}')
