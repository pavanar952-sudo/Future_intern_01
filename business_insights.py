import pandas as pd
import os


# ---------------------------------------
# 1. Load Historical Sales
# ---------------------------------------

historical = pd.read_csv(
    "dataset/monthly_sales.csv"
)

historical["Date"] = pd.to_datetime(
    historical["Date"]
)


# ---------------------------------------
# 2. Load Future Forecast
# ---------------------------------------

forecast = pd.read_csv(
    "outputs/future_sales_forecast.csv"
)

forecast["Date"] = pd.to_datetime(
    forecast["Date"]
)


# ---------------------------------------
# 3. Historical Sales Analysis
# ---------------------------------------

total_sales = historical["Sales"].sum()

average_monthly_sales = historical["Sales"].mean()

highest_sales_row = historical.loc[
    historical["Sales"].idxmax()
]

lowest_sales_row = historical.loc[
    historical["Sales"].idxmin()
]


# ---------------------------------------
# 4. Forecast Analysis
# ---------------------------------------

average_forecast = forecast[
    "Predicted Sales"
].mean()

highest_forecast_row = forecast.loc[
    forecast["Predicted Sales"].idxmax()
]

lowest_forecast_row = forecast.loc[
    forecast["Predicted Sales"].idxmin()
]


# ---------------------------------------
# 5. Compare Future vs Historical
# ---------------------------------------

future_change = (
    (average_forecast - average_monthly_sales)
    / average_monthly_sales
) * 100


# ---------------------------------------
# 6. Display Business Insights
# ---------------------------------------

print("\n======================================")
print("BUSINESS INSIGHTS")
print("======================================")


print(
    "\nTotal Historical Sales:",
    round(total_sales, 2)
)


print(
    "\nAverage Monthly Historical Sales:",
    round(average_monthly_sales, 2)
)


print(
    "\nHighest Historical Sales:"
)

print(
    "Date:",
    highest_sales_row["Date"].strftime("%B %Y")
)

print(
    "Sales:",
    round(highest_sales_row["Sales"], 2)
)


print(
    "\nLowest Historical Sales:"
)

print(
    "Date:",
    lowest_sales_row["Date"].strftime("%B %Y")
)

print(
    "Sales:",
    round(lowest_sales_row["Sales"], 2)
)


print(
    "\nAverage Forecasted Monthly Sales:",
    round(average_forecast, 2)
)


print(
    "\nHighest Forecasted Sales:"
)

print(
    "Date:",
    highest_forecast_row["Date"].strftime("%B %Y")
)

print(
    "Predicted Sales:",
    round(
        highest_forecast_row["Predicted Sales"],
        2
    )
)


print(
    "\nLowest Forecasted Sales:"
)

print(
    "Date:",
    lowest_forecast_row["Date"].strftime("%B %Y")
)

print(
    "Predicted Sales:",
    round(
        lowest_forecast_row["Predicted Sales"],
        2
    )
)


print(
    "\nExpected Change in Average Monthly Sales:",
    round(future_change, 2),
    "%"
)


# ---------------------------------------
# 7. Business Recommendation
# ---------------------------------------

print("\n======================================")
print("BUSINESS RECOMMENDATION")
print("======================================")


if future_change > 0:

    print(
        "The forecast indicates an increase in "
        "average monthly sales."
    )

    print(
        "The business should consider increasing "
        "inventory and staffing during high-demand "
        "periods."
    )

else:

    print(
        "The forecast indicates a decrease in "
        "average monthly sales."
    )

    print(
        "The business should control inventory levels "
        "and avoid overstocking."
    )


print(
    "\nForecast analysis completed successfully!"
)