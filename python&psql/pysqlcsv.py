import pandas as pd
from getrandata.customnames import get_customer
import psycopg2  # or the appropriate database driver

# Connect to PostgreSQL
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='PyPsqlDb',
    user='pyuser',
    password='pypassword'
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# SQL statement to create the "customer" table
create_table_query = """
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    address VARCHAR(200)
);
"""

# Construct the SQL query
sql = "INSERT INTO customer (name, address, email) VALUES (%s, %s, %s)"

# Execute the query
cursor.execute(sql, (get_customer()['name'], get_customer()['address'], get_customer()['email']))

# Commit the changes to the database
conn.commit()


# Define your SQL query
query = 'SELECT * FROM customer;'

# Execute the query and fetch the results
df = pd.read_sql(query, con=conn)

# Display the retrieved data
print(df)

# Create a DataFrame with your data
data = {'column1': [get_customer()['name'], get_customer()['address'], get_customer()['email'],],
        'column2': [get_customer()['name'], get_customer()['address'], get_customer()['email'],]}
df = pd.DataFrame(data)

# Write the DataFrame to the database table
#df.to_sql(name='customer', con=conn, if_exists='append', index=False)

# Convert the DataFrame to a CSV file
df.to_json('output.json', index=True)
df.to_csv('output.json', index=True)
# Close the cursor and connection
cursor.close()
conn.close()