import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

api_key = os.getenv('api_key')

genres = requests.get('https://api.themoviedb.org/3/genre/movie/list?api_key='+api_key+'&language=en-US').json()
genre_dict={}
for values in genres.values():
    # print(values)
    genresList = values
    # print(genresList)
    for genre in genresList:
        # print(genre)
        genre_dict[genre['name']]= genre['id']


print('Welcome to Movie suggestor, we help you find great shows!')

user_input= input('Please type in a genre of movies you would like to see:  ').capitalize()
if user_input in genre_dict:
    print(f'You have selected {user_input} below is a list of top 10 {user_input} movies available: ')
else:
    print('The genre selected is not available. Please select from list below.')
    [print(key) for key,value in genre_dict.items()]


# movies = requests.get('https://api.themoviedb.org/3/discover/movie?api_key='+api_key+'&language=en-US&with_genres=12&sort_by=vote_average.desc').json()

# top_movies= movies['results'][:11]


