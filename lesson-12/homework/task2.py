import requests
import random

def get_genre_list(api_key):
    """Fetches a list of available movie genres."""
    base_url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {"api_key": api_key, "language": "en-US"}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        genres = response.json()["genres"]
        return {genre["name"]: genre["id"] for genre in genres}
    else:
        raise Exception(f"Failed to fetch genres. HTTP Status Code: {response.status_code}")

def get_movies_by_genre(api_key, genre_id):
    """Fetches movies from a given genre."""
    base_url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": api_key,
        "with_genres": genre_id,
        "language": "en-US",
        "sort_by": "popularity.desc",
        "include_adult": False
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()["results"]
    else:
        raise Exception(f"Failed to fetch movies. HTTP Status Code: {response.status_code}")

def recommend_movie(movies):
    """Recommends a random movie from a list."""
    if not movies:
        return None
    return random.choice(movies)

# Main execution
API_KEY = "your_api_key_here"  # Replace with your TMDb API key

try:
    # Fetch genres
    genres = get_genre_list(API_KEY)
    print("Available Genres:")
    for genre in genres:
        print(genre)

    # Ask user for a genre
    user_genre = input("\nEnter a genre: ").capitalize()
    if user_genre not in genres:
        raise Exception("Genre not found. Please enter a valid genre.")

    # Fetch movies for the chosen genre
    genre_id = genres[user_genre]
    movies = get_movies_by_genre(API_KEY, genre_id)

    # Recommend a random movie
    movie = recommend_movie(movies)
    if movie:
        print(f"\nRecommended Movie:\nTitle: {movie['title']}\nOverview: {movie['overview']}")
    else:
        print("No movies found for the selected genre.")

except Exception as e:
    print(e)
