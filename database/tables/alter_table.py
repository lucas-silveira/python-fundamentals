from mysql.connector import ProgrammingError
from config import new_connection

sql = 'ALTER TABLE contacts ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY'

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql)

    except ProgrammingError as err:
        print(f'Erro: {err.msg}')
