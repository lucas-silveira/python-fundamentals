from mysql.connector import ProgrammingError
from config import new_connection

sql = 'INSERT INTO contacts (name, phone) VALUES (%s, %s)'
args = ('John', '1004-4321')

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, args)
        connection.commit()
    except ProgrammingError as err:
        print(f'Erro: {err.msg}')
    else:
        print('1 registro inserido, ID:', cursor.lastrowid)
