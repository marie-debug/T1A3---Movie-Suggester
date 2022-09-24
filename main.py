import os
from dotenv import load_dotenv
import requests
import helpers as hp
import json

load_dotenv()

api_key = os.getenv('api_key')

genres_result = requests.get(
    'https://api.themoviedb.org/3/genre/movie/list?api_key='+api_key+'&language=en-US').json()


genre_names = hp.genre_dictionary(genres_result)

user_input = ''


def get_trending_movies():
    """
    Gets a list of trending movies
    """
    trending_shows = hp.get_data(
        'https://api.themoviedb.org/3/trending/all/day?api_key='+api_key)

    for show in trending_shows:
        if 'name' in show:
            print('\n================================')
            print('Title: ' + show['name'])
            print('Summary: ' + show['overview'])
            print('Original_language: ' + show['original_language'])
        elif 'title' in show:
            print('\n================================')
            print('Title: ' + show['title'])
            print('Summary: ' + show['overview'])
            print('Original_language: ' + show['original_language'])


def get_top_movies(genre_input):
    """
    Gets the top movies in the database for the given genre
    """
    top_movies = hp.get_data('https://api.themoviedb.org/3/discover/movie?api_key='+api_key +
                             '&language=en-US&with_genres='+str(genre_names[genre_input])+'&sort_by=vote_average.desc')
    for movie in top_movies:
        print('\n================================')
        print('Title: ' + movie['title'])
        print('Summary: ' + movie['overview'])  
    return top_movies

def get_upcoming_movies():
    """
    Gets all top 10 upcoming movies with their title release date and overview in the database
    """
    upcoming_movies = hp.get_data(
        'https://api.themoviedb.org/3/movie/upcoming?api_key='+api_key + '&language=en-US&page=1')
    for movie in upcoming_movies:
        print('\n================================')
        print('Title: ' + movie['title'])
        print('Summary: ' + movie['overview'])
        print('Release date: ' + movie['release_date'])

def create_file(filename,data):
    user_file_input =input('would you like to save this list? (yes/no): ')
    if user_file_input == 'yes':
        with open(filename+".txt", "w",encoding="utf8") as f:
             for dict in data:
                f.write(f"Title:{dict['title']}\n\nSummary:\n\n{dict['overview']}\n================================\n\n")



while user_input != 'q':
    print("\nWelcome to Movie suggestor, we help you find great shows!")
    print("\n[trend] Enter Trend to get top 10 trending movies and shows.")
    print("\n[genre] Enter genre name eg horror, action to get top 10 movies and shows based on genres.")
    print("\n[latest] Enter Latest to get top 10 upcoming movies and shows.")
    print("\n[q] Enter q to quit.")

    user_input = input(
        "\nWhat would you like to do?:  ").lower()
    expected_user_input = ['trend','genre','q','latest']
    if user_input not in expected_user_input:
        print("\nYou must enter either trend, genre ,latest or q ")

    if user_input == 'genre':

        genre_input = ''

        while genre_input not in genre_names:
            genre_input = input(
                "\n[2] Enter genre name eg horror, action to get top 10 movies and shows based on genres: ")

            if genre_input in genre_names:
                print(
                    f'\nYou have selected {genre_input} below is a list of top 10 {genre_input} movies available:\n ')
                data = get_top_movies(genre_input)
                create_file('trending movies',data)
            else:
                print(
                    'The genre selected is not available. Please select from list below.')
                [print(key) for key, value in genre_names.items()]

    elif user_input == 'trend':
        print(
            f'\nYou have selected {user_input} below is a list of top 10 trending movies available:\n ')

        get_trending_movies()
       
    elif user_input == 'latest':
        print(
            f'\nYou have selected {user_input} below is a list of top 10 upcoming movies:\n ')

        get_upcoming_movies()

    elif user_input == 'q':
        print("\nMay the Force be with you.\n")


print("Thanks again, we hope to see you soon ! Hasta la vista, baby.")
