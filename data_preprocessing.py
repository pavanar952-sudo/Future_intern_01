import pandas as pd

# ---------------------------------------
# 1. Load Dataset
# ---------------------------------------

file_path = "dataset/Sample - Superstore.csv"

df = pd.read_csv(file_path, encoding="latin1")

print("Dataset loaded successfully!")
print("Original shape:", df.shape)


# ---------------------------------------
# 2. Remove Duplicate Rows
# ---------------------------------------

duplicates = df.duplicated().sum()

print("Duplicate rows:", duplicates)

df = df.drop_duplicates()


# ---------------------------------------
# 3. Convert Order Date
# ---------------------------------------

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
)


# ---------------------------------------
# 4. Convert Sales to Numeric
# ---------------------------------------

df["Sales"] = pd.to_numeric(
    df["Sales"],
    errors="coerce"
)


# ---------------------------------------
# 5. Remove Invalid Rows
# ---------------------------------------

df = df.dropna(
    subset=["Order Date", "Sales"]
)


# ---------------------------------------
# 6. Sort Data by Date
# ---------------------------------------

df = df.sort_values(
    by="Order Date"
)


# ---------------------------------------
# 7. Display Cleaned Data
# ---------------------------------------

print("\nCleaned dataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nFirst 5 cleaned rows:")
print(df.head())


# ---------------------------------------
# 8. Create Month Column
# ---------------------------------------

df["Month"] = df["Order Date"].dt.to_period("M")


# ---------------------------------------
# 9. Calculate Monthly Sales
# ---------------------------------------

monthly_sales = (
    df.groupby("Month")["Sales"]
      .sum()
      .reset_index()
)


# ---------------------------------------
# 10. Convert Month to Date
# ---------------------------------------

monthly_sales["Month"] = monthly_sales["Month"].dt.to_timestamp()


# Rename columns
monthly_sales.columns = ["Date", "Sales"]


# ---------------------------------------
# 11. Save Monthly Dataset
# ---------------------------------------

monthly_sales.to_csv(
    "dataset/monthly_sales.csv",
    index=False
)


# ---------------------------------------
# 12. Display Monthly Sales
# ---------------------------------------

print("\nMonthly Sales:")
print(monthly_sales.head(10))

print("\nMonthly sales dataset saved successfully!")

print("\nNumber of months:")
print(len(monthly_sales))