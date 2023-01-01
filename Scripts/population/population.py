import yaml
import pandas as pd
from faker import Faker
from sys import argv
from connection import create_db_connection, Error
import random
from faker import Faker
from query_actions import read_query, execute_query
fake = Faker(["pt_PT"])

# creating a connection
connection = create_db_connection("localhost", "root", argv[1], "dorlux")

def write_on_file(query):
    f = open("population_script.txt", "a")
    f.write(query)
    f.close()


def populate_client():
    query = "INSERT INTO client (idClient, VAT, contact) \n\tVALUES \n\t"
    listaux = list(range(1,31))
    random.shuffle(listaux)
    execute_query(connection, "DELETE FROM client")
    for i in range(1,31):
        NIF = random.randint(100000000,999999999)
        fk = listaux[i-1]
        if i<=29:
          query += f"({i}, {NIF}, {fk}), \n\t"
        else:
          query += f"({i}, {NIF}, {fk});\n\n"
    execute_query(connection, query)
    write_on_file(query)

def populate_client_has_address():
    query = "INSERT INTO client_has_address (Client_idClient, Address_idAdress) \n\tVALUES \n\t"
    iniCliente = 1
    fimCliente = 10
    execute_query(connection, "DELETE FROM client_has_address")
    for j in range(1,4):        #1-10    11-20    21-30       #10 20 30
        clientes = list(range(iniCliente, fimCliente))
        moradas = list(range(1,10))
        random.shuffle(clientes)
        random.shuffle(moradas)
        

        for i in range(9):
            query += f"({clientes[i]}, {moradas[i]}),\n\t"
        
        y = random.randint(0,8)

        if j == 3:
           query += f"({j*10}, {moradas[y]});\n\n"
        else:
           query += f"({j*10}, {moradas[y]}),\n\t"

        iniCliente += 10
        fimCliente += 10
    execute_query(connection, query)
    write_on_file(query)
    


def populate_category():
    with open("category.yaml", "r") as file_stream:
        instances = yaml.safe_load(file_stream)
    
    query = "INSERT INTO category (idCategory, name, descripton, tax)\n\tVALUES"

    execute_query(connection, "DELETE FROM category")
    for pk, key in enumerate(instances, start=1):
        instance = instances[key]
        query += f"\n\t('{pk}', '{instance['name']}', '{instance['description']}', '{instance['tax']}'),"

    query = query[:-1] + ";\n\n"
    execute_query(connection, query)
    write_on_file(query)


def populate_item():
    with open("item.yaml", "r") as file_stream:
        instances = yaml.safe_load(file_stream)
    
    query = "INSERT INTO item (idItem, name, description, stockNr, priceBuy, priceSell, category)\n\tVALUES"

    execute_query(connection, "DELETE FROM Item")
    for pk, key in enumerate(instances, start=1):
        instance = instances[key]
        query += f"\n\t('{pk}', '{instance['name']}', '{instance['desc']}', '{instance['stockNr']}', '{instance['priceBuy']}', '{instance['priceSell']}', '{instance['category']}'),"
    
    query = query[:-1] + ";\n\n"
    execute_query(connection, query)
    write_on_file(query)

def populate_contact():
    query = "INSERT INTO contact (idContact, name, email, phone) \n\tVALUES"
    

    execute_query(connection, "DELETE FROM contact")
    for i in range(1,31):
        name = fake.name()
        email = fake.email()
        phone_nr = random.randint(910000000,969999999)
    
        query += f"\n\t('{i}', '{name}', '{email}', '{phone_nr}'),"
        
    query = query[:-1] + ";\n\n"
    execute_query(connection, query)
    write_on_file(query)
    

def populate_address():
    print("Populating address table ............")

    query = "INSERT INTO address (idAdress, street, zipCode, city)\n\tVALUES"
    
    execute_query(connection, "DELETE FROM address")
    for i in range(1, 10):
        query += f"\n\t('{i}', '{fake.street_address()}', '{fake.postcode()}', '{fake.city()}'),"

    query = query[:-1] + ";\n\n"
    execute_query(connection, query)
    write_on_file(query)    



populate_contact()
populate_client()
populate_address()
populate_client_has_address()
populate_category()
populate_item()


    
