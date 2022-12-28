import pandas as pd
from sys import argv
from connection import create_db_connection, Error

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        return result
    except Error as err:
        print(f"Error: '{err}'")

# creating a connection
connection = create_db_connection("localhost", "root", argv[1], "dorlux")


execute_query(connection, "INSERT INTO address VALUES ('7', 'ASDAS', 'ASDDAS', 'ADSAD')")
read_query(connection, "SELECT * FROM address")

