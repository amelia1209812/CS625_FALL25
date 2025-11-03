# HW5 - Analyzing Data Using Distribution Charts

Amelia Ragsdale

CS 625, Fall 2025

Date: November 2nd, 2025

## Part 1: Resident Population - States (1970 - 2009)

**Data Preparation and Manipulation**

The dataset was cleaned to remove any non-state entries and unnecessary columns such as postal abbreviations and ANSI codes. The year columns were coverted to numeric values and then reshaped to a long format for easier visualization and analysis. The missing values were then identified and excluded for plotting to ensure optimal accuracy.

**Boxplot - State Populations in 1970, 1985, 1995, and 2009**

![Boxplot](Boxplot_HW5.png)

**Explanation:**

The boxplots highlight the central tendency, spread, and outliers in the states populations. By comparing the multiple years, trends such as population growth and increasing disparities are easy detect. Outliers represent the states with exceptionally high populations relative to the rest of the country.

**Advantages, Disadvantages, and Observations**

The boxplots are incredibly useful because they provide a clear picture of the median, quartiles, and extremes for the state populations, allowing for the quick identification of states with unusually high or low populations. They also enable the comparisons across mulitiple years, making it easy to detect trends with population growth and/or disparity. However, the boxplots do not provide detailed information about individual states beyond outliers, and they may be less intuitive for audiences unfamiliar with quartile-based visualizations. Observing the boxplots, it is evident that the median population has steadily increased from 1970 to 2009, while the spread of the populations widened. Outliers such as California and Texas became more prominent over time, indicating concentrated growth in a few states, whereas smaller states show relatively slower increases.


**Histogram - Distribution of State Populations in 2009**

![Histogram](Histogram_HW5.png)

**Explanation:**

The histogram shows the frequency distribution of state populations for 2009, highlighting how many states fall into different population ranges. Bin sizes ere chosen to balance the detail with reliability, providing a clear overview of population distribution.

**Advantages, Disadvantages, and Observations**

Histograms reveal clustering and gaps within the data, maing it easy to identify population ranges with the highest frequencies. They also highlight the skewness and potentional modes in the distribution, which then can guide further analysis of the data. On the downside, the choice of bin width does affect perception, too wide may hide important details and too narrow can create noise, and outliers sometimes cannot stand out clearly. Observations from the histogram indicated that most of the states have populations between 500,000 and 5,000,000, while a few high populated states (California and Texas) stand out as the extreme right-skewed outliers. This observation confirms that population growth is concentrated in a small number of states.

**eCDF - State Population Distributions (1970 vs. 2009)**

![eCDF](eCDF_HW5.png)

**Explanation:**

The eCDF shows the cumlative proportion of states below each population level which allows the direct comparison of distributions between two years without relying on binning. Horizontal shifts in the graph indicate the overall population growth, while slopes provide insight into the distribution spread.

**Advantages, Disadvantages, and Observations**

The eCDF presents the entire distribution without the need for arbitrary bins, allowing for easy comparison of multiple years. It also highlights how much of the population lies below certain thresholds. However, it may be less intuitive for audiences unfamiliar with cumulative distributions, and extreme outliers are less visually emphasized than in boxplots. By observing the eCDF graph, the 2009 curve is shifted to the right, indicating overall population growth, and its slope is less steep, reflecting increased disparity among states. The eCDF confirms that larger states are growing faster than smaller states, emphasizing the growing population gap over time.
  
## Part 2: Further Analysis and Findings

**Chart: Top 5 Populated States in 2009**
![Top5Pop_2009](Top5Pop_2009.png)

**Findings**

California, Texas, New York, Florida, and Illinois were the top five most populated states in 2009. California had more than twice the population of Illinois, highlighting the concentration of population in a few states. This suggests that urbanization, economic opportunities, and migration patterns heavily influence state population sizes.

**Chart: Population Growth by State**
![BarChart_HW5](BarChart_HW5.png)

**Findings:**

Southern and Western states, including Nevada, Arizona, and Florida, experiecned higher growth rates compared to many Northeastern and Midwestern states. Economic development, climate, and migration trends likely contributed to these regional differences. Some traditionally smaller states, such as Utah and Colorado, show exponential growth relative to their initial population.

**Chart: Heatmap of State Populations Over Time**
![Heatmap_HW5](Heatmap_HW5.png)

**Findings:**

The heatmap shows the gradual population growth for most states over the decades. Rapid growth is apparent in Southern and Western states, while slower growth or stagnation is visible in parts of Midwest and Northeast. The heatmap is useful for identifying regional trends and anomalies, such as states with increased rapid growth due to economic boom. Pleas

***Insights:***

*The population growth is highly concentrated in a few states which is affecting towards political representation and resources allocation. This is evident from both the boxplots and the histograms. Regional growth disparities are evident with Western and Southern states who consistently experience higher growth rates than Northern and Midwestern states. This pattrn is shows in the eCDF and heatmap charts.*



## References

- Github, *Dataset Folder*, <https://github.com/odu-cs625-datavis/public-fall25-mcw/blob/main/datasets/10s0498.xls>
- United States Census, *Population*, <https://www.census.gov/library/publications/2010/compendia/statab/130ed/population.html>
- Microsoft, *Python Support in Visual Studio on Windows*, <https://learn.microsoft.com/en-us/visualstudio/python/overview-of-python-tools-for-visual-studio?view=vs-2022>
- Openpyxl, *openpyxl - A Python library to read/write Excel 2010 xlsx/xlsm files*, <https://openpyxl.readthedocs.io/en/stable/>
- GeekforGeeks, *Python | Pandas.melt()*, <https://www.geeksforgeeks.org/python/python-pandas-melt/>
