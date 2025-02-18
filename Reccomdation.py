import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the original dataset
df = pd.read_csv('/Users/saahithkalakuntla/Desktop/movies.csv')

# Selecting only the columns we need
columns_needed = ['original_title', 'genres', 'overview', 'release_date', 'vote_average']
df_subset = df[columns_needed].head(500)

# Cleaning up the data
df_subset = df_subset.fillna('')  # Replace any NaN values with empty strings
df_subset = df_subset.reset_index(drop=True)  # Reset the index to start from 0

# Save the cleaned subset to a new CSV file
df_subset.to_csv('movies_subset_500.csv', index=False)

# Now load the subset for the recommendation system
df = pd.read_csv('movies_subset_500.csv')


# Feature selection: Using only Title, Genres, and Overview
df['combined_features'] = df['original_title'] + " " + df['genres'] + " " + df['overview']

# User query
user_query = input("Enter Query: ")

# Text Vectorization using TF-IDF
# TF-IDF (Term Frequency-Inverse Document Frequency) converts text to numerical vectors
vectorizer = TfidfVectorizer(
    stop_words='english',  # Remove common English words
    max_features=5000,     
    ngram_range=(1, 2)     
)

# Convert movie descriptions to vectors
movie_vectors = vectorizer.fit_transform(df['combined_features'])

# Convert user query to vector
query_vector = vectorizer.transform([user_query])

# Calculate cosine similarity between query and all movies
print("Calculating similarities...")
similarity_scores = cosine_similarity(query_vector, movie_vectors)

# Rank movies by similarity
df['similarity'] = similarity_scores[0]
recommendations = df.sort_values(by='similarity', ascending=False).head(5)

# Display results
print("Top Recommendations:")
print(recommendations[['original_title', 'similarity']])