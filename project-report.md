Semester Project: Exploring Inequities in Internet Access Across Virginia Communities
Amelia Ragsdale
CS 625, Fall 2025
Due: December 7, 2025

---

## GITHUB REPOSITORY & CODE

- **Project Repository:** [Insert your GitHub repo URL here]  
- **Python Implementation of Final Chart:** [Insert link to Python file or notebook for scatterplot and bar charts here]  

This repository contains all data cleaning, processing, and visualization code used to generate the final charts. The code is fully reproducible, and all charts can be recreated by running the Python scripts with the provided CSV files.

---

## DATA

For this project, I analyzed data on internet access and household income across Virginia counties. The datasets were obtained from the **U.S. Census Bureau’s American Community Survey (ACS) 5-Year Estimates**:  

- **Internet Subscriptions in Households:** Number of households in each Virginia county with internet subscriptions.  
  [Link to dataset](https://www.census.gov/programs-surveys/acs/)  
- **Median Household Income:** Median income per county.  
  [Link to dataset](https://www.census.gov/programs-surveys/acs/)

I cleaned the datasets by selecting only the necessary columns, converting string values to numeric, and removing missing or invalid entries. After cleaning, I merged the two datasets on the county name to align all variables correctly. To facilitate comparison across counties of different sizes, I calculated a derived variable, `Internet_Access_Pct`, representing the percentage of households with internet access relative to the county with the highest number of households. This metric allows fair comparison and makes the scatterplot more interpretable.

---

## SCATTERPLOT: INTERNET ACCESS VS MEDIAN HOUSEHOLD INCOME

**Idiom:** Scatterplot  
**Marks:** Points (circles)  
**Data:** Median Household Income (quantitative), Internet Access (%) (quantitative), County Type (categorical/color), Number of Households (quantitative/size)  
**Encode:**  
- x-axis → Median Household Income  
- y-axis → Internet Access (%)  
- color → County Type (Urban vs. Rural)  
- size → Number of Households with Internet  

The scatterplot shows the relationship between median household income and internet access across Virginia counties. Higher-income counties tend to have higher internet access percentages, but several counties classified as urban behave more like rural counties, with lower-than-expected access. These outliers are annotated with arrows to highlight misclassifications or infrastructure limitations.  

The use of point size to represent the number of households provides additional context about the scale of each county, while color distinguishes between urban and rural counties. The chart title, “Higher-Income Virginia Counties Have Better Internet Access — But Several ‘Urban’ Counties Behave Like Rural Outliers,” succinctly summarizes the main insight. The scatterplot effectively communicates both the general trend and the exceptions, making it easier to understand how inequities persist.

**Figure: Scatterplot showing Internet Access (%) vs Median Household Income**  
![Insert scatterplot image here](path_to_scatterplot_image.png)

---

## TOP 10 COUNTY BAR CHART

**Idiom:** Bar Chart  
**Marks:** Rectangles (bars)  
**Data:** County (categorical), Internet Access (%) (quantitative)  
**Encode:**  
- x-axis → County  
- y-axis → Internet Access (%)  

The top 10 bar chart highlights counties with the highest percentage of households with internet access. These counties are predominantly urban or higher-income areas. Bar charts make it easy to compare individual counties and quickly identify those with the best access.

**Figure: Top 10 Counties for Internet Access (%)**  
![Insert top 10 bar chart image here](path_to_top10_bar_chart_image.png)

---

## BOTTOM 10 COUNTY BAR CHART

**Idiom:** Bar Chart  
**Marks:** Rectangles (bars)  
**Data:** County (categorical), Internet Access (%) (quantitative)  
**Encode:**  
- x-axis → County  
- y-axis → Internet Access (%)  

The bottom 10 bar chart emphasizes counties with the lowest internet access percentages, which are mostly rural and lower-income counties. Together with the top 10 chart, this visualization reinforces the disparities in broadband availability across Virginia.

**Figure: Bottom 10 Counties for Internet Access (%)**  
![Insert bottom 10 bar chart image here](path_to_bottom10_bar_chart_image.png)

---

## DEVELOPMENT AND RECREATION OF CHARTS

I recreated these visualizations in Python using Pandas, Seaborn, Matplotlib, and the `adjustText` library. This allowed precise control over axis labels, point sizes, colors, and annotations. The `adjustText` library prevented overlapping labels in the scatterplot, and the legend was customized to show approximate household counts without including column names.  

Creating the charts required careful data cleaning, especially converting raw ACS data to a usable format and computing the derived percentage metric. Identifying outlier counties and adjusting labels took significant effort but improved readability and highlighted interesting findings. Python provided reproducibility and flexibility that allowed me to create clean, high-quality static charts suitable for analysis and presentation.

---

## FINAL THOUGHTS

This project demonstrates inequities in internet access across Virginia counties. The analysis shows that while higher income is strongly associated with better access, administrative urban/rural classifications can obscure real-world disparities. Some urban counties have surprisingly low internet access, indicating that infrastructure gaps and other local factors affect connectivity beyond income.  

The project reinforced the importance of careful data cleaning, thoughtful visual encoding, and annotation in creating explanatory visualizations. Using scatterplots and bar charts together allowed me to communicate both trends and exceptions effectively. Overall, this project strengthened my ability to combine data from multiple sources, calculate meaningful derived metrics, and create clear, interpretable visualizations.

---

## REFERENCES

- U.S. Census Bureau, American Community Survey (ACS) 5-Year Estimates: Internet Subscriptions in Households and Median Household Income. [https://www.census.gov/programs-surveys/acs/](https://www.census.gov/programs-surveys/acs/)  
- Python libraries: Pandas, Seaborn, Matplotlib, adjustText
