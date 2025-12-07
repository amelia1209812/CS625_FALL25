import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

# -------------------------------------------------------
# 1. LOADING CSV DATA FILES
# -------------------------------------------------------
internet_df = pd.read_csv('/Users/ameliaragsdale/Desktop/Semester_Project/Internet-Subscription/internet_subscription.csv')
income_df = pd.read_csv('/Users/ameliaragsdale/Desktop/Semester_Project/Median-Income/median_income.csv')

# -----------------------------------------------------------
# 2. KEEPING THE ONLY NEEDED COLUMNS +  THEN RENAMING THEM
# -----------------------------------------------------------
internet_df = internet_df[['NAME', 'S2802_C01_001E']]
internet_df.rename(columns={'NAME':'County','S2802_C01_001E':'Internet_Households'}, inplace=True)

income_df = income_df[['NAME','B19013_001E']]
income_df.rename(columns={'NAME':'County','B19013_001E':'Median_Income'}, inplace=True)

# -------------------------------------------------------
# 3. CLEANING THE STRING + NUMERIC VALUES
# -------------------------------------------------------
internet_df['County'] = internet_df['County'].str.strip()
income_df['County'] = income_df['County'].str.strip()

internet_df['Internet_Households'] = pd.to_numeric(internet_df['Internet_Households'], errors='coerce')
income_df['Median_Income'] = pd.to_numeric(income_df['Median_Income'], errors='coerce')

internet_df.dropna(subset=['Internet_Households'], inplace=True)
income_df.dropna(subset=['Median_Income'], inplace=True)

# -------------------------------------------------------
# 4. MERGING THE DATASETS
# -------------------------------------------------------
merged_df = pd.merge(internet_df, income_df, on='County')

# -------------------------------------------------------
# 5. COMPUTING THE INTERNET ACCESS PERCENTAGE
# -------------------------------------------------------
merged_df['Internet_Access_Pct'] = merged_df['Internet_Households'] / merged_df['Internet_Households'].max() * 100

# -------------------------------------------------------
# 6. CREATE THE COUNTY TYPE
# -------------------------------------------------------
merged_df['County_Type'] = merged_df['Internet_Households'].apply(lambda x: 'Urban' if x>50000 else 'Rural')

# ------------------------------------------------------------------
# 7. SCATTERPLOT - INTERNET ACCESS VS MEDIAN INCOME (FINAL CHART)
# ------------------------------------------------------------------
from adjustText import adjust_text
import matplotlib.patches as mpatches

plt.figure(figsize=(12,6))

# Scatter plot with point sizes proportional to Internet_Households 
sns.scatterplot(
    data=merged_df,
    x='Median_Income',
    y='Internet_Access_Pct',
    hue='County_Type',
    size='Internet_Households',
    sizes=(20, 200),
    palette={'Urban':'blue','Rural':'red'},
    alpha=0.7,
    legend=False  
)

plt.title(
    "Higher-Income Virginia Counties Have Better Internet Access —\n But Several ‘Urban’ Counties Behave Like Rural Outliers",
    fontsize=12
)
plt.xlabel("Median Household Income ($)")
plt.ylabel("Internet Access (%)")
plt.grid(True)

# The 3 extreme outliers to note
texts = []
outliers = merged_df.sort_values('Internet_Access_Pct').head(3)
for idx, row in outliers.iterrows():
    texts.append(
        plt.text(
            row['Median_Income'],
            row['Internet_Access_Pct'],
            row['County'],
            fontsize=8,
            rotation=30
        )
    )
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='black'))

# Scatterplot legend
# Color legend (County Type)
urban_patch = mpatches.Patch(color='blue', label='Urban')
rural_patch = mpatches.Patch(color='red', label='Rural')

# Size legend (rounded, readable)
legend_markers = [
    plt.scatter([], [], s=20, color='gray', alpha=0.7),
    plt.scatter([], [], s=110, color='gray', alpha=0.7),
    plt.scatter([], [], s=200, color='gray', alpha=0.7)
]

plt.legend(
    handles=[urban_patch, rural_patch] + legend_markers,
    labels=['Urban', 'Rural', '~2k households', '~25k households', '~1.1M households'],
    title='County Type & Internet Households',
    bbox_to_anchor=(1.05,1),
    loc='upper left'
)

plt.tight_layout()
plt.show()

# -------------------------------------------------------
# 8. TOP & BOTTOM 10 COUNTY BAR GRAPHS
# -------------------------------------------------------
sorted_df = merged_df.sort_values(by='Internet_Access_Pct', ascending=False)

top10 = sorted_df.head(10)
bottom10 = sorted_df.tail(10)

# ------- TOP 10 BAR CHART ---------------------------------
plt.figure(figsize=(14,6))
sns.barplot(
    data=top10,
    x='County',
    y='Internet_Access_Pct'
)
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Counties in Virginia for Internet Access (%)')
plt.xlabel('County')
plt.ylabel('Internet Access (%)')
plt.tight_layout()
plt.show()

# ------ BOTTOM 10 BAR CHART ---------------------------------
plt.figure(figsize=(14,6))
sns.barplot(
    data=bottom10,
    x='County',
    y='Internet_Access_Pct'
)
plt.xticks(rotation=45, ha='right')
plt.title('Bottom 10 Counties in Virginia for Internet Access (%)')
plt.xlabel('County')
plt.ylabel('Internet Access (%)')
plt.tight_layout()
plt.show()
