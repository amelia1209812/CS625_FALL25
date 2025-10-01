import pandas as pd
import matplotlib.pyplot as plt

# Load CSV, skip empty row
df = pd.read_csv("/Users/ameliaragsdale/Documents/Untitled spreadsheet - 2010.csv", skiprows=4)

# Rename the first column
df = df.rename(columns={"Unnamed: 0": "Living arrangement"})

# Drop rows that aren’t actual categories (Total, NaN, PERCENT)
df = df.dropna(subset=["Living arrangement"])  # removes NaN row
df = df[~df["Living arrangement"].isin(["Total (1,000)", "PERCENT"])]  # removes totals/percent row

# Check cleaned data
print(df.head())

# Living arrangement vs 30–44 years old
plt.figure(figsize=(10,6))
plt.bar(df["Living arrangement"], df["30 to 44 years old.3"])
plt.xticks(rotation=45, ha="right")
plt.title("Living arrangement for 30–44 year olds")
plt.xlabel("Living arrangement")
plt.ylabel("Population (1,000s)")
plt.tight_layout()
plt.show()
