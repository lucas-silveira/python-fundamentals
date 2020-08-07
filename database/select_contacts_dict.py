from mysql.connector import ProgrammingError
from config import new_connection

sql = 'SELECT * FROM contacts LIMIT %s OFFSET %s'

with new_connection() as connection:
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql, (10, 0))
        contacts = cursor.fetchall()
    except ProgrammingError as err:
        print(f'Erro: {err.msg}')
    else:
        for contact in contacts:
            print(
                f'{contact["id"]:2d} - {contact["name"]:10s} Telefone:\
                    {contact["phone"]}')
