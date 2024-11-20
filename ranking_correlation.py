import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data for sports rankings
ranking_data = {
    'Sport': ['Boxing', 'Ice Hockey', 'Football', 'Basketball', 'Wrestling',
              'Martial Arts', 'Tennis', 'Gymnastics', 'Baseball/Softball', 'Soccer'],
    'Rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Total': [72.375, 71.750, 68.375, 67.875, 63.500,
              63.375, 62.750, 62.500, 62.250, 61.500]
}

# Data for viewership percentages (2023)
viewership_data = {
    'Sport': ['Football', 'Basketball', 'Baseball', 'Boxing',
              'Ice Hockey', 'Soccer', 'Golf', 'MMA', 'Tennis', 'Motorsports'],
    'Viewership (%)': [74.5, 56.6, 50.5, 23.4,
                       22.1, 21.6, 19.7, 16.7, 15.5, 14.6]
}

# Convert to DataFrame
rank_df = pd.DataFrame(ranking_data)
viewership_df = pd.DataFrame(viewership_data)

# Merge DataFrames on Sport
merged_df = pd.merge(rank_df, viewership_df, on='Sport', how='outer')

# Check for NaN values and fill them with zeros if necessary
merged_df.fillna(0, inplace=True)

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 6))

# Bar plot for Rankings
ax1.bar(merged_df['Sport'], merged_df['Rank'], color='b', alpha=0.6, label='Rank')
ax1.set_ylabel('Ranking (Lower is Better)', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Set y-limits for rankings
ax1.set_ylim(0, max(merged_df['Rank']) + 1)

# Create a second y-axis for Viewership
ax2 = ax1.twinx()
ax2.plot(merged_df['Sport'], merged_df['Viewership (%)'], color='r', marker='o', label='Viewership (%)')
ax2.set_ylabel('Viewership (%)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Title and Legends
plt.title('Sports Rankings vs Viewership Percentages in the USA')
fig.tight_layout()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()