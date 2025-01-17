import pandas as pd

# Load the IPL dataset 
df = pd.read_csv('C:/Users/Rahul/Desktop/ipl_matches_smalldata.csv')

# Sort the dataset by the 'total_runs' column (assuming the column is named 'total_runs')
top_10_players = df.sort_values(by='total_runs', ascending=False).head(10)

# Calculate the mean of the total_runs scored by top 10 players
mean_runs = top_10_players['total_runs'].mean()

# Calculate the mode of the total_runs scored by top 10 players
mode_runs = top_10_players['total_runs'].mode()[0]  # mode() returns a Series, so we take the first value

# Print the results
print(f"Mean total_runs scored by the top 10 players: {mean_runs}")
print(f"Mode of total_runs scored by the top 10 players: {mode_runs}")
