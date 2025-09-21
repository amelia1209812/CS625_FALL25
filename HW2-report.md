# Homework 2: Data Cleaning

Amelia Ragsdale  
CS 625, Fall 2025  
Due: September 21, 2025

## Part 1. Data Cleaning

### Explanation

For this assignment, I used OpenRefine to clean the PetNames dataset in preparation for analysis in Part 2. I focused on key colums such as the kind of pet, pet name, pet full name, age, and breed, all of which contained significant inconsistencies and irrelevant data. My goal was not to perfectly clean the entire dataset, but to clean enough by using GREL, clustering, facets, and manual edits to ensure meaningful and accurate analysis could be performed after the cleaning.

For the "**kind of pet**" column, the data was very inconsistent. There were many varioated in capitalization (like "Dog", "dog", "DOG") as well as completely unrelated entried (like cardboard cut out). I started by applying a **Text Facet** to quickly see all unique values and used **clustering** to further merge varioations of common animal types. However, due to the amount of unusual entries and misspellings that it couldn't be resolved through clustering, I also had to do significiant amount of manual cleaning in this columns. This included filtering out irrelevant rows and standardizing terms to a consistent format (ex. "puppy" to "Dog").

For the **pet name** column, I used a similar approach. I began with a **Text Facet** and used **clustering** to identify and merge variations of the same name, such as "bella", "Bella", and "BELLA". I also applied **GREL transformations** to standardize capitalization account all names using expressions like `value.toTitlecase()` and `value.trim()` to clean up any whitespace and casing issues. I also used the expression `value.replace("'","")` to remove unwanted characters that were leftover in the different pet names. Some names had multiple entries or special characters that clustering didn't resolve well, so I made targeted **manual edits** to fix those as well.

In the **pet full name** column, I followed the same process: clustering to merge similar entries, and GREL to handle formatting. I used expressions like `values.toTitlecase()` to fix the inconsistent capitalization, and `if(isBlank(value), "Unknown", value)` to fil in missing or blank entries withha default value of "Unknown". This helped reduce noise and made the column more consistent for analysis.

The **age** column was by far the most difficult and time-consuming to clean. It included a wide variety of inconsistent and irrelevant enteries such as "puppy", "baby", "born in 2015", and specific ages like "10 months", "2 years", and "~5". I started by filtering the colums by used facets to identify valid age entries and listed rows as "Unknown" if it couldn't be used for numeric analysis. I chose to keep only those enteries that specified age in either weeks, months, or year. I attempted to normalize the age values using **GREL expressions** to convert months to decimal years (ex. 6 months = 0.5 ) and to extract numbers from strings. One expression I used was:

`if(value.toLowercase().contains("month"),
  toNumber(value.toLowercase().split(" ")[0]) / 12,
  if(value.toLowercase().contains("year"),
    toNumber(value.toLowercase().split(" ")[0]),
    null
  )
)
`
However, while testing several variations of the above **GREL expression**, I accidentally applied a expression that wiped out the entire column, deleting all the age values. Fortunately, I was able to recover my work by using OpenRefine's **Undo/Redo history**, which allowed me to revert the changes and start over. After recovering the data, I attempted to complete additional cleaning using both **clustering** and **manual edits**. In the end, I retained only cleaned enteries where the age was clearly expressed in weeks, months, or number of year.

In conclusion, across all columns I made extensive use of **GREL transformations**, including `value.toTitlecase()` for capitalization, `value.trim()` to remove extra spaces, `value.replace(" and ", ",")` to separate multi-pet names, and `f(isBlank(value), "Unknown", value)` to fill in missing data. I avoided using RegEx heavily after some earlier expressions caused errors or unexpected deletions. For columns that did not require numeric conversion, I focused on consistency, formatting, and removing unwanted characters. While I relied heavily on OpenRefine’s powerful features like facets, clustering, and transformations, I also made targeted manual edits when automated methods weren’t effective. In particular, the “kind of pet” and “age” columns required the most manual attention due to the wide variety of inconsistent, messy, or irrelevant entries.



 

## Markdown

### Q1 - Bulleted List

- Apples
- Bananas
- Grapes

A bulleted list is unordered which means the items do not have a specific sequence. A numbered list is ordered and further implies that the order or ranking of items is important such as steps in a process.

### Q2 - Markdown Paragraph

I was walking through the *interfimensional potato farm* when I stumbled upon a **talking llama** who whispered, "***Never trust a penguin with sunglasses***." Confused, I typed `llama.speak("Hello, traveler!")` into my reality debugger and suddenly a portal opened. If this sounds absurd, you're not alone; real more about these phenomena at the [Society for the Bizarre Agricultural Incidents](https://www.youtube.com/watch?v=dQw4w9WgXcQ).

### Q3 - Animal Image

![This is a picture of my German Shepherd mix, Nala. (She is the brown and black dog on the right)](mydog_nala.JPG) This image of my dog was uploaded to the same directory as my report file and is displayed using the MArkdown image syntax.
