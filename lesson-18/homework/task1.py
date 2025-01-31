import pandas as pd
import sqlite3

# 1. Read customers table from chinook.db
conn = sqlite3.connect("chinook.db")
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print("First 10 rows of customers table:")
print(customers_df.head(10))

# 2. Load iris.json
iris_df = pd.read_json("iris.json")
print("\nShape of iris dataset:", iris_df.shape)
print("Column names:", iris_df.columns.tolist())

# 3. Load titanic.xlsx
titanic_df = pd.read_excel("titanic.xlsx")
print("\nFirst 5 rows of titanic dataset:")
print(titanic_df.head())

# 4. Read Flights parquet file
flights_df = pd.read_parquet("flights.parquet")
print("\nSummary of flights dataset:")
print(flights_df.info())

# 5. Load movie.csv
movie_df = pd.read_csv("movie.csv")
print("\nRandom sample of 10 rows from movie dataset:")
print(movie_df.sample(10))