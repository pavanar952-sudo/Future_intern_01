import subprocess
import sys


def run_file(filename):
    print("\n" + "=" * 60)
    print(f"Running: {filename}")
    print("=" * 60)

    result = subprocess.run(
        [sys.executable, filename]
    )

    if result.returncode != 0:
        print(f"\nError while running {filename}")
        sys.exit(result.returncode)


# ---------------------------------------
# Run Complete Project
# ---------------------------------------

print("=" * 60)
print("SALES & DEMAND FORECASTING SYSTEM")
print("=" * 60)

# Step 1: Data preprocessing
run_file("data_preprocessing.py")

# Step 2: Visualization
run_file("visualization.py")

# Step 3: Model training and evaluation
run_file("model_training.py")

# Step 4: Future forecasting
run_file("forecasting.py")

# Step 5: Business insights
run_file("business_insights.py")

print("\n" + "=" * 60)
print("PROJECT COMPLETED SUCCESSFULLY!")
print("=" * 60)