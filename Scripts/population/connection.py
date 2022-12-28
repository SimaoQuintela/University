from mysql.connector import Error, connect

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection