import pandas as pd
import random
import numpy as np

num_records = 1000
years = range(1970, 2024)
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Documentary', 'Romance', 'Sci-Fi', 'Thriller']
durations = range(60, 180)  

data = {
    'type': ['Movie'] * num_records,
    'title': [f'Movie {i+1}' for i in range(num_records)],
    'release_year': [random.choice(years) for _ in range(num_records)],
    'genre': [random.choice(genres) for _ in range(num_records)],
    'duration': [random.choice(durations) for _ in range(num_records)]
}

df = pd.DataFrame(data)

df.to_csv('netflix_data.csv', index=False)
