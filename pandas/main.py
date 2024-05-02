# Import Libraries and Load Data
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV using Pandas
data = pd.read_csv("IMDB top 1000.csv")

# Clean and Prepare Data
# Check for missing values
print(data.isnull().sum())

# Drop any rows with missing values
data.dropna(inplace=True)

# Analyze Ratings Distribution
# Histogram for vote_average distribution
plt.figure(figsize=(8, 6))
plt.hist(data['vote_average'], bins=10, edgecolor='black')
plt.title("Distribution of Movie Ratings")
plt.xlabel("Vote Average")
plt.ylabel("Number of Movies")
plt.grid(True)
plt.tight_layout()
plt.show()

# Correlate Ratings and Popularity
# Calculate the correlation between "vote_average" and "vote_count" (number of votes)
correlation = data['vote_average'].corr(data['vote_count'])
print("Correlation between ratings and popularity: ", correlation)

# Analyze Genre-wise Ratings
# Group data by "genre" and calculate the average rating for each genre
genre_ratings = data.groupby('genre')['vote_average'].mean()

# Create a bar chart to visualize average ratings across different genres
plt.figure(figsize=(10, 6))
genre_ratings.plot(kind='bar')
plt.title("Average Ratings by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.grid(True)
plt.tight_layout()
plt.show()