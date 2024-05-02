import mysql.connector

try:
    # Connect to the database
    cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='harshlogin')

    # Create a cursor object
    cursor = cnx.cursor()

    # Execute a query
    query = "SELECT * FROM accounts"
    cursor.execute(query)

    # Check if the query execution was successful
    if cursor is not None:
        # Fetch the results
        results = cursor.fetchall()

        # Print the results
        for row in results:
            print(row)

except mysql.connector.Error as err:
    # Handle the error
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if cursor is not None:
        cursor.close()
    if cnx is not None:
        cnx.close()