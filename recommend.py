import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
ratings_data = {
    'userId': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4],
    'movieId': [1, 2, 3, 1, 4, 2, 3, 5, 1, 2, 3, 5],
    'rating': [5, 4, 3, 4, 5, 5, 4, 3, 2, 4, 5, 5]
}

ratings = pd.DataFrame(ratings_data)
ratings.to_csv('ratings.csv', index=False)

# Sample movies data
movies_data = {
    'movieId': [1, 2, 3, 4, 5],
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E']
}

movies = pd.DataFrame(movies_data)
movies.to_csv('movies.csv', index=False)

# Load the data
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

# Merge the ratings and movies data
data = pd.merge(ratings, movies, on='movieId')

# Create a pivot table
user_movie_matrix = data.pivot_table(index='userId', columns='title', values='rating')

# Fill missing values with 0
user_movie_matrix.fillna(0, inplace=True)

# Calculate the cosine similarity matrix
user_similarity = cosine_similarity(user_movie_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

# Function to get movie recommendations for a user
def get_user_similar_movies(user_id, num_recommendations=5):
    # Get the user's ratings
    user_ratings = user_movie_matrix.loc[user_id]

    # Get the similarity scores for this user with all other users
    similar_users = user_similarity_df[user_id]

    # Sort users by similarity score
    similar_users = similar_users.sort_values(ascending=False)

    # Weigh the ratings of similar users by their similarity score
    weighted_ratings = pd.Series(0, index=user_movie_matrix.columns)
    for i in range(1, len(similar_users)):
        similar_user_id = similar_users.index[i]
        similar_user_ratings = user_movie_matrix.loc[similar_user_id]
        weighted_ratings += similar_user_ratings * similar_users.iloc[i]

    # Drop the movies the user has already rated
    watched_movies = user_ratings[user_ratings > 0].index
    weighted_ratings = weighted_ratings.drop(watched_movies, errors='ignore')

    # Sort the weighted ratings and get the top recommendations
    recommendations = weighted_ratings.sort_values(ascending=False).head(num_recommendations)
    return recommendations.index.tolist()

# Example: Get recommendations for user with ID 1
recommended_movies = get_user_similar_movies(1)
print(f"Recommended movies for user 1: {recommended_movies}")
