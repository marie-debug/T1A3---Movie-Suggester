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

print('Welcome to Movie suggestor, we help you find great shows!')
print('here is a list of trending shows')
trending= requests.get('https://api.themoviedb.org/3/trending/all/day?api_key='+api_key).json()
trending_shows= trending['results'][:11]

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

while True:
    user_input = input(
        'Please type in a genre of movies you would like to see:  ').capitalize()

    if user_input in genre_names:
        print(
            f'You have selected {user_input} below is a list of top 10 {user_input} movies available: ')
        break
    else:
        print('The genre selected is not available. Please select from list below.')
        [print(key) for key, value in genre_names.items()]


movies = requests.get('https://api.themoviedb.org/3/discover/movie?api_key='+api_key +
                      '&language=en-US&with_genres='+str(genre_names[user_input])+'&sort_by=vote_average.desc').json()

top_movies = movies['results'][:11]

for movie in top_movies:
    print('\n================================')
    print('Title: ' + movie['title'])
    print('Summary: ' + movie['overview'])

upcoming_movies_response = requests.get('https://api.themoviedb.org/3/movie/upcoming?api_key='+api_key +'&language=en-US&page=1').json()

upcoming_movies=upcoming_movies_response['results'][:11]

for movie in upcoming_movies:
    print('\n================================')
    print('Title: ' + movie['title'])
    print('Summary: ' + movie['overview'])
    print('Release date: ' + movie['release_date'])
