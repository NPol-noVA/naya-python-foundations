# Nutrition Data Analysis
## Dataset

 Dataset file: 'nutr.csv'


## Introduction

 This project analyzes a public nutrition dataset stored in the file nutr.csv. The dataset contains nutrition and health-related information collected from different locations and demographic groups. Important variables include Data_Value, LocationDesc, Topic, Question, and confidence limit measurements.
 The objective of this project is to load the dataset, inspect its structure, clean the data, and perform basic statistical analysis using Python and Pandas.

## Dataset Description

 The dataset contains information related to nutrition and health indicators across different locations. Each record represents a measurement associated with a specific health topic and population group.

## Key Columns
 LocationDesc – Location or state name.
 Topic – Health or nutrition topic.
 Question – Survey question being measured.
 Data_Value – Numeric value representing the measurement.
 Low_Confidence_Limit – Lower confidence interval.
 High_Confidence_Limit – Upper confidence interval.

## Load and Inspect
 The dataset was loaded into a Pandas DataFrame using:

    import pandas as pd

    rf = pd.read_csv("nutr.csv", low_memory=False)

 The following inspection steps were performed:

 1.Display the dataset shape using rf.shape.
 2.Display the column names using rf.columns.
 3.Display the data types using rf.dtypes.
 4.Display the first five rows using rf.head().

 These steps helped identify the structure and contents of the dataset before analysis.

## Data Cleaning

The dataset contained missing values in the Low_Confidence_Limit column.

### Cleaning Method

Rows containing missing values in this column were removed using:

         rf = rf.dropna(subset=["Low_Confidence_Limit"])
        
 Explanation

Removing missing values improves data quality and ensures that subsequent calculations and analyses are based on complete records.

## Analysis

Question 1: What is the average Data_Value?

        Code
        
        rf["Data_Value"].mean()

Result

Average Data_Value: ________

Interpretation

This value represents the overall average measurement across all records in the dataset.

Question 2: What is the maximum Data_Value?

        Code
        
        rf["Data_Value"].max()

Result

Maximum Data_Value: ________

Interpretation

This is the highest recorded value in the dataset.

Question 3: Which location has the highest average Data_Value?

        Code
        
        rf.groupby("LocationDesc")["Data_Value"].mean().sort_values(ascending=False)

Result

Location with the highest average Data_Value: ________
Average value: ________

Interpretation

This location recorded the highest average measurement among all locations in the dataset.

## Conclusion

The nutrition dataset was successfully loaded, inspected, cleaned, and analyzed using Pandas. Missing values were identified and removed to improve data quality. Basic statistical analysis was performed to calculate the average and maximum Data_Value values and identify the location with the highest average Data_Value. These results provide useful insights into the nutritional measurements recorded in the dataset.
