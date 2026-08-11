import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn.linear_model import LinearRegression


# ---------------------------------------
# 1. Load Monthly Sales Data
# ---------------------------------------

file_path = "dataset/monthly_sales.csv"

df = pd.read_csv(file_path)

print("Monthly sales data loaded successfully!")


# ---------------------------------------
# 2. Convert Date Column
# ---------------------------------------

df["Date"] = pd.to_datetime(df["Date"])


# ---------------------------------------
# 3. Create Time-Based Features
# ---------------------------------------

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Quarter"] = df["Date"].dt.quarter
df["Time_Index"] = range(len(df))


# ---------------------------------------
# 4. Define Features and Target
# ---------------------------------------

features = [
    "Time_Index",
    "Year",
    "Month",
    "Quarter"
]

X = df[features]
y = df["Sales"]


# ---------------------------------------
# 5. Train Model Using All Historical Data
# ---------------------------------------

model = LinearRegression()

model.fit(X, y)

print("Model trained successfully!")


# ---------------------------------------
# 6. Find Last Historical Date
# ---------------------------------------

last_date = df["Date"].max()

print("\nLast historical date:", last_date)


# ---------------------------------------
# 7. Create Next 12 Months
# ---------------------------------------

future_dates = pd.date_range(
    start=last_date + pd.DateOffset(months=1),
    periods=12,
    freq="MS"
)


# ---------------------------------------
# 8. Create Future Features
# ---------------------------------------

future_df = pd.DataFrame({
    "Date": future_dates
})

future_df["Year"] = future_df["Date"].dt.year
future_df["Month"] = future_df["Date"].dt.month
future_df["Quarter"] = future_df["Date"].dt.quarter

future_df["Time_Index"] = np.arange(
    len(df),
    len(df) + 12
)


# ---------------------------------------
# 9. Predict Future Sales
# ---------------------------------------

future_X = future_df[features]

future_predictions = model.predict(
    future_X
)

future_df["Predicted Sales"] = future_predictions


# ---------------------------------------
# 10. Create Outputs Folder
# ---------------------------------------

os.makedirs("outputs", exist_ok=True)


# ---------------------------------------
# 11. Save Forecast
# ---------------------------------------

future_df.to_csv(
    "outputs/future_sales_forecast.csv",
    index=False
)


# ---------------------------------------
# 12. Display Forecast
# ---------------------------------------

print("\n======================================")
print("NEXT 12 MONTH SALES FORECAST")
print("======================================")

print(
    future_df[
        ["Date", "Predicted Sales"]
    ].to_string(index=False)
)

print("\nFuture forecast saved successfully!")


# ---------------------------------------
# 13. Plot Historical + Future Forecast
# ---------------------------------------

# ---------------------------------------
# 13. Business-Friendly Forecast Graph
# ---------------------------------------

plt.figure(figsize=(14, 7))

# Historical sales
plt.plot(
    df["Date"],
    df["Sales"],
    marker="o",
    linewidth=2,
    label="Historical Sales"
)

# Forecasted sales
plt.plot(
    future_df["Date"],
    future_df["Predicted Sales"],
    marker="o",
    linestyle="--",
    linewidth=2,
    label="Forecasted Sales"
)


# ---------------------------------------
# 14. Mark Forecast Start
# ---------------------------------------

plt.axvline(
    x=last_date,
    linestyle="--",
    linewidth=1.5,
    label="Forecast Start"
)


# ---------------------------------------
# 15. Graph Details
# ---------------------------------------

plt.title(
    "Historical Sales and 12-Month Sales Forecast",
    fontsize=17
)

plt.xlabel(
    "Date",
    fontsize=12
)

plt.ylabel(
    "Sales",
    fontsize=12
)

plt.legend()

plt.grid(
    True,
    alpha=0.3
)

plt.xticks(
    rotation=45
)

plt.tight_layout()


# ---------------------------------------
# 16. Save Graph
# ---------------------------------------

plt.savefig(
    "outputs/final_sales_forecast.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(
    "Final sales forecast graph saved successfully!"
)