import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid')

netflix_df = pd.read_csv('netflix_data.csv')
netflix_movies_df = netflix_df[netflix_df['type'] == 'Movie'].copy()
netflix_movies_df['duration'] = netflix_movies_df['duration'].astype(str).str.replace(' min', '').astype(int)

plt.figure(figsize=(16, 8))
top_genres = netflix_movies_df['genre'].value_counts().head(5).index
filtered_df = netflix_movies_df[netflix_movies_df['genre'].isin(top_genres)]
sns.scatterplot(data=filtered_df, x='release_year', y='duration', hue='genre', alpha=0.3)
plt.title('Movie Duration by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Duration (minutes)')
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

avg_duration_per_year = filtered_df.groupby('release_year')['duration'].mean().reset_index
