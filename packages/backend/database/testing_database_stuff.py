import mysql.connector
from mysql.connector import Error


def make_mysql_connection(host_name, user_name, user_password):
    connection = None
    print(f"Starting a Connection from {host_name} as user {user_name}")
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as e:
        print(f"Error: '{e}'")

    return connection


def create_database(cursor, database_name):
    print(f"Attempting to create database: {database_name}")
    try:
        cursor.execute(f"CREATE DATEBASE {database_name}")
        print("Database created successfully")
    except Error as e:
        print(f"Error: '{e}'")


if __name__ == '__main__':
    HOST_NAME = 'localhost'
    USER_NAME = 'marsj'
    USER_PASSWORD = ''

    mysql_connection = make_mysql_connection(HOST_NAME, USER_NAME, USER_PASSWORD)
    mysql_cursor = mysql_connection.cursor()

    db_name = ''
    create_database(mysql_cursor, db_name)

