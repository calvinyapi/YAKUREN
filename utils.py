from Model import Product
from myPostgreSQL import connexionPSQL

conn = connexionPSQL("amazon", "localhost", "postgres", "root", "5432")

cur = conn.cursor()

def list_product():
    # Execute a query
    cur.execute("SELECT * FROM Product")
    records = cur.fetchall()
    print(records)
    return records


def create_product(data: Product):
    query = "INSERT INTO Product (name, price, description) VALUES (%s, %s, %s);"
    cur.execute(query, (data.name, data.price, data.description))
    conn.commit()
    cur.closed()
    return f"Product '{data.name}' added successfully."


def create_client(lastname: str, firstname: str, age: int, email: str, id_user_type: int):
    query = "INSERT INTO Users (firstname, lastname, age, email, id_user_type) VALUES (%s, %s, %s, %s, %s);"
    cur.execute(query, (firstname, lastname, age, email, id_user_type))
    conn.commit()
    cur.closed()

def order_client(id_user: int, id_product: int, quantity: int, status: str):
    query = "INSERT INTO product_orders (id_user, id_product, quantity, status) VALUES (%s, %s, %s, %s);"
    cur.execute(query, (id_user, id_product, quantity, status))
    conn.commit()
    cur.closed()
    return f"Productc '{id_product}' ordered"

# User
