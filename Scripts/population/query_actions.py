from mysql.connector import Error

def execute_query(connection, query):
    cursor = connection.cursor()
    print(query)
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