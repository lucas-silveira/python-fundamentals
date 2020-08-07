from mysql.connector import ProgrammingError
from config import new_connection

sql = 'DELETE FROM contacts WHERE id = %s'
args = (4,)

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, args)
        connection.commit()
    except ProgrammingError as err:
        print(f'Erro: {err.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) deletado(s).')
