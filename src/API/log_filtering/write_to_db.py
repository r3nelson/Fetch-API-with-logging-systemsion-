import psycopg2

# Connect to the PostgreSQL database
def connect_to_db():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="ChangeMe",  # Change this to the password you set
            host="localhost",
            port="5432",
            database="postgres"  # Change this to the name of your database
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None

# Insert data into a table
def insert_data(connection, data):
    cursor = connection.cursor()
    try:
        # Example: Insert data into a table named 'logs'
        insert_query = "INSERT INTO logs (timestamp, log_level, message) VALUES (%s, %s, %s)"
        # Execute the query with the data
        cursor.execute(insert_query, data)
        connection.commit()
        print("Data inserted successfully")
    except (Exception, psycopg2.Error) as error:
        print("Error while inserting data into PostgreSQL", error)
    finally:
        # Close the cursor
        cursor.close()

# Example data
data_to_insert = ('2024-01-22 13:04:15,890', 'ERROR', '"http://localhost:4000/mangadddd" was not found')

# Connect to the database
connection = connect_to_db()

# Insert data into the database
if connection is not None:
    insert_data(connection, data_to_insert)
    # Close the database connection
    connection.close()
else:
    print("Unable to connect to the database.")
