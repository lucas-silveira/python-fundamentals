from mysql.connector import ProgrammingError
from config import new_connection

contacts_table = '''
  CREATE TABLE contacts(
    name VARCHAR(50),
    phone VARCHAR(40)
  )
'''

emails_table = '''
  CREATE TABLE emails(
    id INT AUTO_INCREMENT PRIMARY KEY,
    owner VARCHAR(50)
  )
'''

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(contacts_table)
        cursor.execute(emails_table)
    except ProgrammingError as err:
        print(f'Erro: {err.msg}')
