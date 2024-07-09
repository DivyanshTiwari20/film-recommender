import requests

TMDB_API_KEY = 'e553994b1cd16af11c0d89bfa4041f17'
TMDB_BASE_URL = 'https://api.themoviedb.org/3'

def get_movies_by_genre(genre_id, language='en-US', page=1):
    url = f"{TMDB_BASE_URL}/discover/movie"
    params = {
        'api_key': TMDB_API_KEY,
        'with_genres': genre_id,
        'language': language,
        'page': page
    }
    response = requests.get(url, params=params)
    return response.json()

def get_movie_details(movie_id, language='en-US'):
    url = f"{TMDB_BASE_URL}/movie/{movie_id}"
    params = {
        'api_key': TMDB_API_KEY,
        'language': language
    }
    response = requests.get(url, params=params)
    return response.json()
