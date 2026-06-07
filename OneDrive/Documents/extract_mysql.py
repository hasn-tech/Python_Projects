import mysql.connector
import pandas as pd

def extract_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="sales"
    )

    query = "SELECT * FROM orders"
    df = pd.read_sql(query, conn)

    df.to_csv("orders.csv", index=False)
    print("Data extracted successfully")

if __name__ == "__main__":
    extract_data()