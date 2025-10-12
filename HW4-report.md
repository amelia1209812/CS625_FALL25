## HW4 - Arrange Tables
Amelia Ragsdale
CS 625, Fall 2025
Date: October 12, 2025

## Question 1: Total DoD Personnel by Branch (1960–2008)

## Line Chart:
Insert image of line chart here (e.g., dod_q1_linechart.png)

## Idiom-Mark-Data-Encode Table:

Element	Details
Idiom	Line chart
Mark	Line + point markers
Data	Total personnel by branch, 1960–2008
Encoding	x → Year (position), y → Personnel (position), color → Branch

## Explanation:

A line chart effectively shows trends over time for multiple branches.

Using distinct colors and markers allows clear differentiation between branches.

Grid lines improve readability of year-by-year changes.

## Insights:

Army and Navy have historically had the largest personnel.

The Air Force shows a decline in personnel after the 1990s.

The Marine Corps maintains relatively steady numbers.

## Design Decisions / Customizations:

Marker points added to emphasize each year’s data.

Grid lines added to improve readability.

Figure size set for clear visibility of all lines.

## Question 2: Male vs Female Enlisted Personnel by Branch (2008)

## Chart:
Insert image of stacked/grouped bar chart here (e.g., dod_q2_gender.png)

## Idiom-Mark-Data-Encode Table:

Element	Details
Idiom	Stacked / grouped bar chart
Mark	Bar
Data	Male and female personnel by branch in 2008
Encoding	x → Branch (position), y → Count (length), color → Gender

## Explanation:

A bar chart allows direct comparison of male vs female personnel within each branch.

Colors clearly distinguish genders.

Ordering branches along the x-axis supports visual comparison across the branches.

## Insights:

Male personnel dominate in all branches.

Air Force has the highest female proportion (~X%), while Marine Corps has the lowest (~Y%). (Replace X/Y with actual numbers from chart)

Highlights the gender distribution within military branches.

## Design Decisions / Customizations:

Rotated x-axis labels for readability.

Added clear legend for gender.

Used grouped bars instead of stacked bars to make individual counts more visible.

## Further Questions

How has female representation changed over time across branches?

Are there correlations between total personnel trends and major military events?

How does total DoD personnel compare with population trends (extra credit)?

## References

2010 Statistical Abstract of the United States, Table 498

Python pandas documentation

Seaborn documentation

Any code examples used in Colab notebooks
