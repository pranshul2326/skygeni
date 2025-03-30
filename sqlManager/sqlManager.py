import sqlite3
from utility.config_path import get_data_file_path
from utility.csvManager import read_csv_file,write_csv_file
def sqlManager(sql_query):
    # Connect to an in-memory SQLite database
    finanical_info_df = read_csv_file(get_data_file_path("finanical_info"))
    client_info_df = read_csv_file(get_data_file_path("client_info"))
    payment_info_df = read_csv_file(get_data_file_path("payment_info"))
    subscription_info_df = read_csv_file(get_data_file_path("subscription_info"))

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

     # Store DataFrames as table
    finanical_info_df.to_sql("finanical_info_table", conn, if_exists="append", index=False)
    client_info_df.to_sql("client_info_table", conn, if_exists="replace", index=False)
    payment_info_df.to_sql("payment_info_table", conn, if_exists="replace", index=False)
    subscription_info_df.to_sql("subscription_info_data", conn, if_exists="replace", index=False)
    cursor.execute(sql_query)

     # Fetch results if it's a SELECT query
    columns = [desc[0] for desc in cursor.description]  # Column names
    rows = cursor.fetchall()  # Get all results
    conn.close()
    print(columns)  # Column names
    print(rows)  # Data rows
    print("Query executed successfully.")

    # Close connection at the end
    conn.close()
