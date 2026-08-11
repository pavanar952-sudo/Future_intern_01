import pandas as pd
import matplotlib.pyplot as plt
import os


# ---------------------------------------
# 1. Load Prediction Results
# ---------------------------------------

file_path = "outputs/model_predictions.csv"

df = pd.read_csv(file_path)

df["Date"] = pd.to_datetime(df["Date"])


# ---------------------------------------
# 2. Create Output Folder
# ---------------------------------------

os.makedirs("outputs", exist_ok=True)


# ---------------------------------------
# 3. Actual vs Predicted Graph
# ---------------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    df["Date"],
    df["Actual Sales"],
    marker="o",
    linewidth=2,
    label="Actual Sales"
)

plt.plot(
    df["Date"],
    df["Predicted Sales"],
    marker="o",
    linestyle="--",
    linewidth=2,
    label="Predicted Sales"
)


# ---------------------------------------
# 4. Graph Details
# ---------------------------------------

plt.title(
    "Actual vs Predicted Sales",
    fontsize=16
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

plt.grid(True)

plt.xticks(rotation=45)

plt.tight_layout()


# ---------------------------------------
# 5. Save Graph
# ---------------------------------------

plt.savefig(
    "outputs/actual_vs_predicted.png",
    dpi=300
)

plt.show()

print("Actual vs Predicted graph saved successfully!")