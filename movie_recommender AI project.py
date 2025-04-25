
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load data
ratings = pd.read_csv('u.data', sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])
movies = pd.read_csv('u.item', sep='|', encoding='latin-1', usecols=[0, 1], names=['movie_id', 'title'])

# Merge ratings with movie titles
df = pd.merge(ratings, movies, on='movie_id')

# Create user-movie matrix
user_movie_matrix = df.pivot_table(index='user_id', columns='title', values='rating')

# Function to recommend movies
def get_recommendations(movie_title, min_ratings=100):
    if movie_title not in user_movie_matrix.columns:
        return f"Movie '{movie_title}' not found in dataset."
    
    movie_ratings = user_movie_matrix[movie_title]
    similar_movies = user_movie_matrix.corrwith(movie_ratings)
    corr_df = pd.DataFrame(similar_movies, columns=['correlation'])
    corr_df.dropna(inplace=True)

    # Add number of ratings
    rating_counts = df.groupby('title').size()
    corr_df['num_ratings'] = rating_counts
    filtered_df = corr_df[corr_df['num_ratings'] > min_ratings]

    return filtered_df.sort_values('correlation', ascending=False).head(10)

# Example usage
if __name__ == '__main__':
    movie = input("Enter a movie title (e.g., Star Wars (1977)): ")
    print("\nTop Recommendations:\n")
    print(get_recommendations(movie))
