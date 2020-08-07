from mysql.connector import connect

connection = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='mysql'
)

cursor = connection.cursor()
cursor.execute('CREATE DATABASE schedule')
