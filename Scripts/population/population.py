from sys import argv
from connection import create_db_connection, Error
import yaml

def execute_query(connection, query):
    cursor = connection.cursor()
    print(query)
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def pupulate_category():
    with open("category.yaml", "r") as file_stream:
        instances = yaml.safe_load(file_stream)
    
    execute_query(connection, "DELETE FROM category")
    for pk, key in enumerate(instances, start=1):
        instance = instances[key]
        sql = f"INSERT INTO category VALUES ('{pk}', '{instance['name']}', '{instance['description']}', '{instance['tax']}')"
        execute_query(connection, sql)

def pupulate_item():
    with open("item.yaml", "r") as file_stream:
        instances = yaml.safe_load(file_stream)
    
    execute_query(connection, "DELETE FROM Item")
    for pk, key in enumerate(instances, start=1):
        instance = instances[key]
        sql = f"INSERT INTO Item VALUES ('{pk}', '{instance['name']}', '{instance['desc']}', '{instance['stockNr']}', '{instance['priceBuy']}', '{instance['priceSell']}', '{instance['category']}')"
        execute_query(connection, sql)

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

pupulate_category()
pupulate_item()
read_query(connection, "SELECT * FROM Address")

