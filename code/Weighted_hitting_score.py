import csv

# Define weights for each statistic
weights = {
    "xba": 0.30,
    "exit_velocity_avg": 0.20,
    "sweet_spot_percent": 0.15,
    "barrel_batted_rate": 0.15,
    "solidcontact_percent": 0.10,
    "hard_hit_percent": 0.10,
}

# Initialize an empty list to store player data
players = []

# Read data from the CSV file
with open("stats.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert numeric values from strings to floats
        for stat in weights.keys():
            row[stat.strip()] = float(row[stat.strip()])
        players.append(row)

# Calculate the composite score for each player
for player in players:
    composite_score = sum(player[stat] * weights[stat.strip()] for stat in weights)
    player["Composite Score"] = composite_score

# Sort players based on their composite scores in descending order
sorted_players = sorted(players, key=lambda x: x["Composite Score"], reverse=True)

# Print the ranked players
print("Ranking of Players based on Composite Score:")
for rank, player in enumerate(sorted_players, start=1):
    print(f"{rank}. {player['﻿last_name']}, {player[' first_name']} - Composite Score: {player['Composite Score']}")
