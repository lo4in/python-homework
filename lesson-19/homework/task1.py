import pandas as pd
import sqlite3

# Connect to the database
conn = sqlite3.connect("chinook.db")

# Load customers and invoices tables
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
invoices_df = pd.read_sql_query("SELECT * FROM invoices", conn)

# Perform an inner join on CustomerId
merged_df = pd.merge(customers_df, invoices_df, on="CustomerId", how="inner")

# Find the total number of invoices for each customer
invoice_counts = merged_df.groupby("CustomerId").size().reset_index(name="Total_Invoices")
print("Total number of invoices for each customer:")
print(invoice_counts.head())