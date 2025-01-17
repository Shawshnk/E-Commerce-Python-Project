# -*- coding: utf-8 -*-
"""E-Commerce Analysis .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JW4LuKiC8iCSkFZPDROm_5eWDLyynuPo
"""

import pandas as pd

df = pd.read_csv('/content/Ecommerce_data.csv')

df.head()

df.columns

"""How many rows & columns in dataset"""

dataframe_shape = df.shape
print(f"The number of rows in dataframe are {dataframe_shape[0]} and columns are {dataframe_shape[1]} ")

df.isnull().sum()

df.dtypes

status = df['delivery_status'].value_counts()
print(status)

"""**Difference betwwen sum & count methods**
sum- sum method calculates the sum of True value in specific columns
count - count method calculate the sum of both True as well as False or non-missing value in the column.

How many orders were delivered ?
"""

delivered_status = (df['delivery_status'] == 'Shipping on time').sum()
print(f"The orders which were delivered successfully :-{delivered_status}")

"""What is the average sales_per_order for each category_name

About Mean & Standard Deviation
Mean- Mean calculate the average value of the value
Standard Deviation- it measures the amount of variation in value. A low standard deviation indicates that the values tend to be close to the mean while a high standard deviation indicates that the values are spread out over a wider range
"""

average_sales_per_order = df.groupby('category_name')['sales_per_order'].mean()
print(f"The average sales_per_order for each category_name is :- {average_sales_per_order}")

"""Which customer_segment has the highest total profit_per_order?"""

customer_segment = df.groupby('customer_segment')['profit_per_order'].sum()
print(f"customer_segment has the highest total profit_per_order is {customer_segment}")

