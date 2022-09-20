import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

api_key = os.getenv('api_key')

genres_result = requests.get('https://api.themoviedb.org/3/genre/movie/list?api_key='+api_key+'&language=en-US').json()
# print(genres_result['genres'])

genresList = genres_result['genres']

genre_dict={}
for genre in genresList:
    # print(genre)
    genre_dict[genre['name']]= genre['id']
# print(genre_dict)


print('Welcome to Movie suggestor, we help you find great shows!')

user_input= input('Please type in a genre of movies you would like to see:  ').capitalize()
if user_input in genre_dict:
    print(f'You have selected {user_input} below is a list of top 10 {user_input} movies available: ')
else:
    print('The genre selected is not available. Please select from list below.')
    [print(key) for key,value in genre_dict.items()]


movies = requests.get('https://api.themoviedb.org/3/discover/movie?api_key='+api_key+'&language=en-US&with_genres='+str(genre_dict[user_input])+'&sort_by=vote_average.desc').json()
# print(movies)

top_movies= movies['results'][:11]
# print(top_movies)

for movie in top_movies:
    print('\n================================')
    print('Title: ' + movie['title'])
    print('Summary: '+ movie['overview'])
  