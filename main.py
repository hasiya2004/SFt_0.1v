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

# Adding sample science data
data['pH_Value'] = np.random.uniform(5.5, 8.5, 10)  # pH values typically range from 0 (very acidic) to 14 (very alkaline), but let's assume our product only varies between 5.5 and 8.5

# Creating the DataFrame
df = pd.DataFrame(data)

# Calculate Total_Sale column
df['Total_Sale'] = df['Quantity_Sold'] * df['Price_Per_Unit']

print(df)
