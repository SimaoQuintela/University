import yaml
import pandas as pd
from faker import Faker
from sys import argv
from connection import create_db_connection, Error
from random import randint, shuffle
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
    shuffle(listaux)

    for i in range(1,31):
        NIF = randint(100000000,999999999)
        fk = listaux[i-1]
        if i<=29:
          query += f"({i}, {NIF}, {fk}), \n\t"
        else:
          query += f"({i}, {NIF}, {fk});\n\n"
    execute_query(connection, query)
    write_on_file(query)

def populate_client_has_address():
    query = "INSERT INTO client_has_address (Client_idClient, Address_idAdress)\n\tVALUES \n\t"
    iniCliente = 1
    fimCliente = 10

    for j in range(1,4):        #1-10    11-20    21-30       #10 20 30
        clientes = list(range(iniCliente, fimCliente))
        moradas = list(range(1,10))
        shuffle(clientes)
        shuffle(moradas)
        

        for i in range(9):
            query += f"({clientes[i]}, {moradas[i]}),\n\t"
        
        y = randint(0,8)

        
        query += f"({j*10}, {moradas[y]}),"

        iniCliente += 10
        fimCliente += 10
    
    query = query[:-1] + ";\n\n"

    execute_query(connection, query)
    write_on_file(query)
    

def populate_category():
    with open("category.yaml", "r") as file_stream:
        instances = yaml.safe_load(file_stream)
    
    query = "INSERT INTO category (idCategory, name, descripton, tax)\n\tVALUES"

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

    for pk, key in enumerate(instances, start=1):
        instance = instances[key]
        query += f"\n\t('{pk}', '{instance['name']}', '{instance['desc']}', '{instance['stockNr']}', '{instance['priceBuy']}', '{instance['priceSell']}', '{instance['category']}'),"
    
    query = query[:-1] + ";\n\n"
    execute_query(connection, query)
    write_on_file(query)

def populate_contact():
    query = "INSERT INTO contact (idContact, name, email, phone) \n\tVALUES"   

    for i in range(1,31):
        name = fake.name()
        email = fake.email()
        phone_nr = randint(910000000,969999999)
        query += f"\n\t('{i}', '{name}', '{email}', '{phone_nr}'),"
        
    query = query[:-1] + ";\n\n"

    execute_query(connection, query)
    write_on_file(query)
    

def populate_address():
    query = "INSERT INTO address (idAdress, street, zipCode, city)\n\tVALUES"
    
    for i in range(1, 10):
        query += f"\n\t('{i}', '{fake.street_address()}', '{fake.postcode()}', '{fake.city()}'),"


    query = query[:-1] + ";\n\n"
    execute_query(connection, query)
    write_on_file(query)

def populate_order():

    query = "INSERT INTO dorlux.Order (idOrder, status, shippingPrice, orderDate, dorlux.order.upDate, Employee, client_idClient)\n\tVALUES"

    for i in range(1, 51):
        query += f"\n\t('{i}', 'PENDING', '{randint(0,5)}.{randint(0,99)}', NOW(), NOW(), '{randint(1,3)}', '{randint(1,30)}'),"

    query = query[:-1] + ";\n\n"
    execute_query(connection, query)
    write_on_file(query)


def populate_employee():

    query = "INSERT INTO employee (idEmployee, manager, salary, contact) VALUES\n\t"

    # Mrs. Dores GIGACHAD
    query += "('1', '1', '1500', '1'),\n\t"
    # Other 2 employees
    query += "('2', '1', '1000', '10'),\n\t('3', '1', '1000', '20');\n\n"

    execute_query(connection, query)
    write_on_file(query)

def populate_order_has_item():
    listaux = list(range(1,51))
    items = list(range(1,4))
    shuffle(listaux)
    query = "INSERT INTO order_has_item (Order_idOrder, Item_idItem, amount) VALUES"

    for i in range(1, 51):
        order = listaux[i-1]
        item = items[randint(0,2)]
        query += f"\n\t('{order}', '{item}', '{randint(1, 20)}'),"

    query = query[:-1] + ";\n\n"

    execute_query(connection, query)
    write_on_file(query)




def delete_all():
    execute_query(connection, "DELETE FROM Order_has_item;")
    execute_query(connection, "DELETE FROM dorlux.Order;")
    execute_query(connection, "DELETE FROM Suplier_provide_item;")
    execute_query(connection, "DELETE FROM Item;")
    execute_query(connection, "DELETE FROM Suplier;")
    execute_query(connection, "DELETE FROM Category;")

    execute_query(connection, "UPDATE Employee SET manager = NULL")
    execute_query(connection, "DELETE FROM Employee;")
    execute_query(connection, "DELETE FROM Client_has_address;")
    execute_query(connection, "DELETE FROM Address;")
    execute_query(connection, "DELETE FROM Client;")
    execute_query(connection, "DELETE FROM Contact;")

#execute_query(connection, "DELETE FROM dorlux.Order;")

delete_all()
# no relation tables

populate_address()
populate_contact()
populate_category()

# relation tables
populate_client()
populate_client_has_address()
populate_item()
populate_employee()

populate_order()
populate_order_has_item()
