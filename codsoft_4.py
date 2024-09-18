# Dictionary of movies with their genres and directors
movies = {
    "The Dark Knight": {"genre": "action", "director": "Christopher Nolan"},
    "Shang-Chi": {"genre": "action", "director": "Destin Daniel Cretton"},
    "Inception": {"genre": "sci-fi", "director": "Christopher Nolan"},
    "The Shawshank Redemption": {"genre": "drama", "director": "Frank Darabont"},
    "The Avengers": {"genre": "action", "director": "Joss Whedon"},
    "Interstellar": {"genre": "sci-fi", "director": "Christopher Nolan"},
    "Pulp Fiction": {"genre": "crime", "director": "Quentin Tarantino"},
    "The Lion King": {"genre": "animation", "director": "Roger Allers"}
}

def recommend_movie(preferred_genre):
    # Filter movies based on the preferred genre
    recommendations = [movie for movie, attributes in movies.items() if attributes["genre"].lower() == preferred_genre.lower()]
    
    # Provide recommendation or a not-found message
    if recommendations:
        return f"I recommend you watch: {', '.join(recommendations)}"
    else:
        return "I'm sorry, I couldn't find a movie in that genre."

# Input from the user
preferred_genre = input("\nWhat genre of movie are you looking for? ").strip()

# Output the recommendation
print(recommend_movie(preferred_genre))
