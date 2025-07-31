import pandas as pd

# Load CSV
df = pd.read_csv("data/products.csv")  # adjust path if needed
df.columns = df.columns.str.strip()    # remove invisible spaces

# Check actual column names
print("📌 Column Names:")
print(list(df.columns))

# Show sample data
print("\n🧪 First 3 rows:")
print(df.head(3))
