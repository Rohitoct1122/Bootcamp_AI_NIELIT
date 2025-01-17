# Import the Pandas library
import pandas as pd

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('C:/Users/Rahul/Desktop/ipl_matches_smalldata.csv')

# Group the data by 'batter' and calculate the total runs scored
runs_scored = df.groupby('batter')['batsman_runs'].sum().reset_index()

runs_scored.columns = ['Player', 'Total Runs']

# Filter players with more than 500 runs
filtered_players = runs_scored[runs_scored['Total Runs'] > 500]

# Print the filtered players
print(filtered_players)
# Load the dataset into a Pandas DataFrame
df = pd.read_csv("ipl_matches.csv")

