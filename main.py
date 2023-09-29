import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Sample sales data
data = {
    'Date': pd.date_range(start='2022-01-01', periods=10, freq='D'),
    'Product_ID': np.random.randint(100, 110, 10),
    'Quantity_Sold': np.random.randint(1, 10, 10),
    'Price_Per_Unit': np.random.uniform(5.0, 20.0, 10)
}
