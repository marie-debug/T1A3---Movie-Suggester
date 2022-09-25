import os
from dotenv import load_dotenv
import requests
import helpers as hp


load_dotenv()

api_key = os.getenv('api_key')


def get_genres():
    """
    Gets the genre names and id in realtime from movie database

    Returns:
        list: list of dictionaries containing genres
    """
    genres_result = requests.get(
        'https://api.themoviedb.org/3/genre/movie/list?api_key='+api_key+'&language=en-US').json()

    genre_names = hp.genre_dictionary(genres_result)
    return genre_names


def get_trending_shows():
    """
    Gets the trending shows in realtime from movie database

    Returns:
        list: list of dictionaries containing trending shows
    """
    trending_shows = hp.get_data(
        'https://api.themoviedb.org/3/trending/all/day?api_key='+api_key)

    hp.print_trending_shows(trending_shows)
    return trending_shows


def get_top_movies(genre_input):
    """
    Gets the top  movies in the database for the given genre

    Args:
        genre_input (string): a string input representing a genre

    Returns:
        list: list of dictionaries representing the top movies title , overview and rating in the database
    """
    genre_names = get_genres()
    top_movies = hp.get_data('https://api.themoviedb.org/3/discover/movie?api_key='+api_key +
                             '&language=en-US&with_genres='+str(genre_names[genre_input])+'&sort_by=vote_average.desc')
    hp.print_top_movies(top_movies)
    return top_movies


def get_upcoming_movies():
    """
    Gets all top upcoming movies with their title release date and overview in the database
    """
    upcoming_movies = hp.get_data(
        'https://api.themoviedb.org/3/movie/upcoming?api_key='+api_key + '&language=en-US&page=1')
    hp.print_upcoming_movies(upcoming_movies)
    return upcoming_movies
