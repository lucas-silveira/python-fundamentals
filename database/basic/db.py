from mysql.connector import connect

connection = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='mysql'
)

if __name__ == '__main__':
    print(connection)
