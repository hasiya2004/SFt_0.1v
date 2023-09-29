
import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Sample sales data
data = {
    'Date': pd.date_range(start='2022-01-01', periods=10, freq='D'),
    'Product_ID': np.random.randint(100, 110, 10),
    'Quantity_Sold': np.random.randint(1, 10, 10),

    'Price_Per_Unit': np.random.uniform(5.0, 20.0, 10),
    'pH_Value': np.random.uniform(5.5, 8.5, 10)
}

# Creating the sales DataFrame
df = pd.DataFrame(data)
df['Total_Sale'] = df['Quantity_Sold'] * df['Price_Per_Unit']

# NASA moon landing data
moon_landings = {
    'Mission': ['Apollo 11', 'Apollo 12', 'Apollo 14', 'Apollo 15', 'Apollo 16', 'Apollo 17'],
    'Date': ['1969-07-20', '1969-11-19', '1971-02-05', '1971-07-30', '1972-04-21', '1972-12-11'],
    'Astronauts': [['Neil Armstrong', 'Buzz Aldrin'], ['Pete Conrad', 'Alan Bean'], ['Alan Shepard', 'Edgar Mitchell'], ['David Scott', 'James Irwin'], ['John Young', 'Charles Duke'], ['Gene Cernan', 'Harrison Schmitt']]
}

moon_df = pd.DataFrame(moon_landings)

# Merging the two datasets on the 'Date' column
merged_df = pd.merge(df, moon_df, on='Date', how='left')

print(merged_df)
=======
    'Price_Per_Unit': np.random.uniform(5.0, 20.0, 10)
}
