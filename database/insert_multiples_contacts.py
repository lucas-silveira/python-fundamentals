from mysql.connector import ProgrammingError
from config import new_connection

sql = 'INSERT INTO contacts (name, phone) VALUES (%s, %s)'
args = (
    ('Alice', '1005-4321'),
    ('Peter', '1006-4321'),
    ('Alex', '1007-4321'),
)

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.executemany(sql, args)
        connection.commit()
    except ProgrammingError as err:
        print(f'Erro: {err.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) inserido(s).')
