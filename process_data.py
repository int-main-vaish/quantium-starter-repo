import pandas as pd

# Read all CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine files
df = pd.concat([df1, df2, df3], ignore_index=True)

# Keep only Pink Morsels
df = df[df["product"] == "pink morsel"]

# Remove $ and convert to float
df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

# Create sales column
df["sales"] = df["quantity"] * df["price"]

# Keep only required columns
output = df[["sales", "date", "region"]]

# Save output
output.to_csv("formatted_sales.csv", index=False)

print("File created successfully!")