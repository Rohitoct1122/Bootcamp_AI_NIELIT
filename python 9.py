# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from a CSV file
df = pd.read_csv('C:/Users/Rahul/Desktop/tips.csv')

# Calculate the number of people in smoking and non-smoking areas
smoking_count = df['Smoking'].value_counts()['Yes']
non_smoking_count = df['Smoking'].value_counts()['No']

# Create a pie chart to compare the percentage of people in smoking and non-smoking areas
plt.figure(figsize=(8, 6))
plt.pie([smoking_count, non_smoking_count], labels=['Smoking', 'Non-Smoking'], autopct='%1.1f%%')
plt.title('Percentage of People in Smoking and Non-Smoking Areas')
plt.show()
