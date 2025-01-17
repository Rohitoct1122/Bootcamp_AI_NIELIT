import pandas as pd

# Load the dataset 
df = pd.read_csv('C:/Users/Rahul/Desktop/student_performance.csv')

# Count the number of rows with missing data
missing_rows = df.isnull().sum(axis=1) > 0  # Check if any column in the row is missing
num_missing_rows = missing_rows.sum()  # Count how many rows have missing data

print(f'Number of rows with missing data: {num_missing_rows}')
