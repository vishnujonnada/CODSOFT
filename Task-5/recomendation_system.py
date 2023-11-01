import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie ratings data
data = pd.read_csv('movie_ratings.csv')

# Pivot the data to create a user-movie matrix
user_movie_matrix = data.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)

# Calculate user-user similarity using cosine similarity
user_similarity = cosine_similarity(user_movie_matrix)

def get_movie_recommendations(user_id, user_similarity, user_movie_matrix):
    user_ratings = user_movie_matrix.loc[user_id]
    similar_users = user_similarity[user_id]
    unrated_movies = user_ratings[user_ratings == 0].index

    recommendations = []

    for movie_id in unrated_movies:
        movie_rating = 0
        total_similarity = 0

        for other_user_id, similarity in enumerate(similar_users):
            if user_movie_matrix.iloc[other_user_id][movie_id] != 0:
                movie_rating += user_movie_matrix.iloc[other_user_id][movie_id] * similarity
                total_similarity += similarity

        if total_similarity > 0:
            predicted_rating = movie_rating / total_similarity
            recommendations.append((movie_id, predicted_rating))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations

user_id = 1
recommendations = get_movie_recommendations(user_id, user_similarity, user_movie_matrix)

print(f"Top movie recommendations for user {user_id}:")
for movie_id, predicted_rating in recommendations:
    print(f"Movie ID: {movie_id}, Predicted Rating: {predicted_rating}")
