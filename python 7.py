# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('C:/Users/Rahul/Desktop/ipl_matches_smalldata.csv')

# Group the data by 'batter' and calculate the total runs scored
runs_scored = df.groupby('batter')['batsman_runs'].sum().reset_index()

# Rename the columns for clarity
runs_scored.columns = ['Player', 'Total Runs']

# Sort the data in descending order based on the total runs scored
runs_scored = runs_scored.sort_values(by='Total Runs', ascending=False)

# Select the top 10 players
top_10_players = runs_scored.head(10)

# Create a bar chart to visualize the number of runs by the top 10 players
plt.figure(figsize=(10, 6))
plt.bar(top_10_players['Player'], top_10_players['Total Runs'])
plt.xlabel('Player')
plt.ylabel('Total Runs')
plt.title('Number of Runs by Top 10 Players')
plt.xticks(rotation=90)  # Rotate the x-axis labels for better readability
plt.tight_layout()  # Adjust the layout to fit the labels
plt.show()
