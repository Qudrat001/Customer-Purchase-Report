 # Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# ------------------------------
# 4. SQL PORTFOLIO (Basic Queries Example)
# ------------------------------

sql_example_query = """
SELECT Customer, SUM([Total Amount]) AS Total_Spent
FROM [data_sql]
GROUP BY Customer
ORDER BY Total_Spent DESC;
"""