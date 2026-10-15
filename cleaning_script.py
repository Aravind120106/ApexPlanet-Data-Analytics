
import pandas as pd

data = {
    "OrderID": [101, 102, 103, 104, 104, 105, 106, 107],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Monitor", "Laptop", "Mouse", "Keyboard"],
    "Quantity": [2, 5, 3, 1, 1, None, 4, 2],
    "Price": [50000, 500, 1500, 8000, 8000, 50000, None, 1500],
    "City": ["Hyderabad", "Mumbai", "Delhi", "hyderabad", "hyderabad", "Chennai", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)
df = df.drop_duplicates()
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["Price"] = df["Price"].fillna(df["Price"].median())
df["City"] = df["City"].str.strip().str.title()
df["TotalSales"] = df["Quantity"] * df["Price"]

df.to_csv("cleaned_sales_data.csv", index=False)

print("Data cleaning completed successfully.")
