python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the SAIFI dataset
data = pd.read_csv('SAIFI.csv')

# Convert 'Year' column to datetime format
data['Year'] = pd.to_datetime(data['Year'], format='%Y')

# Plot the SAIFI trend over the years
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='SAIFI', data=data, marker='o')
plt.title('SAIFI Trend (2013-2025)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('SAIFI Value', fontsize=14)
plt.grid(True)
plt.show()

# Save the plot
plt.savefig('saifi_trend.png')

# Calculate and print summary statistics
mean_saifi = data['SAIFI'].mean()
max_saifi = data['SAIFI'].max()
min_saifi = data['SAIFI'].min()
print(f'Mean SAIFI: {mean_saifi}')
print(f'Max SAIFI: {max_saifi}')
print(f'Min SAIFI: {min_saifi}')

# Example output to CSV
summary = {
    'Mean SAIFI': [mean_saifi],
    'Max SAIFI': [max_saifi],
    'Min SAIFI': [min_saifi]
}
summary_df = pd.DataFrame(summary)
summary_df.to_csv('saifi_summary.csv', index=False)
