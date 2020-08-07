from mysql.connector import ProgrammingError
from config import new_connection

sql = 'SELECT * FROM contacts WHERE phone = %s'

with new_connection() as connection:
    try:
        name = input('Digite um telefone para encontrar um contato: ')
        cursor = connection.cursor()
        cursor.execute(sql, (name,))
    except ProgrammingError as err:
        print(f'Erro: {err.msg}')
    else:
        print(cursor.fetchone())
