import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


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
# 5. Time-Based Train/Test Split
# ---------------------------------------

split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]


print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# ---------------------------------------
# 6. Create Linear Regression Model
# ---------------------------------------

model = LinearRegression()


# ---------------------------------------
# 7. Train Model
# ---------------------------------------

model.fit(X_train, y_train)

print("\nModel trained successfully!")


# ---------------------------------------
# 8. Predict Test Data
# ---------------------------------------

y_pred = model.predict(X_test)


# ---------------------------------------
# 9. Calculate Evaluation Metrics
# ---------------------------------------

mae = mean_absolute_error(
    y_test,
    y_pred
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        y_pred
    )
)

r2 = r2_score(
    y_test,
    y_pred
)


# ---------------------------------------
# 10. Display Model Performance
# ---------------------------------------

print("\n==============================")
print("MODEL PERFORMANCE")
print("==============================")

print("MAE :", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 4))


# ---------------------------------------
# 11. Actual vs Predicted
# ---------------------------------------

results = pd.DataFrame({
    "Date": df["Date"].iloc[split_index:].values,
    "Actual Sales": y_test.values,
    "Predicted Sales": y_pred
})


print("\n==============================")
print("ACTUAL VS PREDICTED SALES")
print("==============================")

print(results.to_string(index=False))


# ---------------------------------------
# 12. Save Results
# ---------------------------------------

results.to_csv(
    "outputs/model_predictions.csv",
    index=False
)

print("\nPrediction results saved successfully!")