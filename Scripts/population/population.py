import pandas as pd
from faker import Faker
from sys import argv
from connection import create_db_connection, Error
import random
from faker import Faker

fake = Faker(["pt_PT"])

# creating a connection
connection = create_db_connection("localhost", "root", argv[1], "dorlux")

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
        
        for entry in result:
            print(entry)
        
        return result
    except Error as err:
        print(f"Error: '{err}'")


def populate_contact(connection):
    query = "INSERT INTO contact (idContact, name, email, phone) \n\tVALUES"

    for i in range(1,31):
        name = fake.name()
        email = fake.email()
        phone_nr = random.randint(910000000,969999999)
        if i <= 29:
           query += f"\n\t('{i}', '{name}', '{email}', '{phone_nr}'),"
        else:
           query += f"\n\t('{i}', '{name}', '{email}', '{phone_nr}');\n\n"
    

    query = ''.join(query)
    #print(query)

    execute_query(connection, query)
    read_query(connection, "SELECT * FROM contact")
    execute_query(connection, "DELETE FROM contact")


    f = open("population_script.txt", "a")
    f.write(query)
    f.close()
    
def populate_address(connection):
    print("Populating address table ............")

    query = ["INSERT INTO address (idAdress, street, zipCode, city)", "\n\tVALUES"]
    # ex:  ('1', 'Rua de Santa Marta', '4750-428', 'Fafe')
    for i in range(1, 10):
        query.append(f"\n\t('{i}', '{fake.street_address()}', '{fake.postcode()}', '{fake.city()}'), ")

    query.append(f"\n\t('{i+1}', '{fake.street_address()}', '{fake.postcode()}', '{fake.city()}');\n\n")

    query = ''.join(query)

    print(query)
    execute_query(connection, query)
    read_query(connection, "SELECT * FROM address")
    execute_query(connection, "DELETE FROM address")

    f = open('population_script.txt', 'a')
    f.write(query)
    f.close()

    return connection 
    





populate_contact(connection)
populate_address(connection)

