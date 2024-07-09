from flask import Flask, request, jsonify, render_template
from tmdb import get_movies_by_genre, get_movie_details
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_preferences = request.json
    genre_id = user_preferences.get('genre_id')
    language = user_preferences.get('language', 'en-US')
    movies = get_movies_by_genre(genre_id, language)
    return jsonify(movies)

# The below code is required for Vercel to detect the app
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

if __name__ == "__main__":
    app.run(debug=True)
