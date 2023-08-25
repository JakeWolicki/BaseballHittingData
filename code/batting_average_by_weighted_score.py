import csv
import matplotlib.pyplot as plt

# Sort players based on their composite scores in descending order
sorted_players = sorted(players, key=lambda x: x["Composite Score"], reverse=True)

# Extract the top 100 players' composite scores and batting averages for plotting
top_100_players = sorted_players[:100]
composite_scores = [player["Composite Score"] for player in top_100_players]
batting_averages = [player["xba"] for player in top_100_players]

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(batting_averages, composite_scores, c='blue', marker='o', label='Top 100 Players')
plt.xlabel('Batting Average')
plt.ylabel('Composite Score')
plt.title('Scatter Plot: Batting Average vs. Composite Score for Top 100 Players')

# Add labels for individual points (player names) for the top 10 players
for i, player_name in enumerate(player_names[:10]):
    plt.annotate(player_name, (batting_averages[i], composite_scores[i]), textcoords="offset points", xytext=(0, 10), ha='center')

# Show the scatter plot
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
