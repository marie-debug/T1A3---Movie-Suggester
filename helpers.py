import requests
from colorama import Fore, Back, Style

def genre_dictionary(genres_result):
    """
    Takes a genres_result list  and converts it to a dictionary

    Args:
        genres_result (list): list of dictionaries with_genres and ids
    Returns:
        _type_: dictionary of dictionaries with_genres and ids
    """
    genres_list = genres_result['genres']
    genre_dict = {}
    for genre in genres_list:
        genre_dict[genre['name'].lower()] = genre['id']
    return genre_dict

def get_data(url):
    """
    Takes a url and returns a list of dictionaries and checks for errors

    Args:
        url (string): a string representing the url to connect  to movie database

    Returns:
        list: a list of dictionaries containing information of each show from the database
        """
    data = []
    try_again_message = "Please try again "
    try:
        response = requests.get(url).json()
        data = response['results'][:11]
    except requests.ConnectionError:
        print("OOPS!! Connection Error. Make sure you are connected to Internet.\n")
        print(try_again_message)
    except requests.Timeout:
        print("OOPS!! Timeout Error")
        print(try_again_message)
    except requests.RequestException:
        print("OOPS!! General Error")
        print(try_again_message)
    return data

def print_text_green(text):
    """converts text color to green

    Args:
        text (string): a string representation  of the text
    """
    print(Fore.GREEN + text)
    print(Style.RESET_ALL)

def print_text_blue(text):
    """converts text color to blue

    Args:
        text (string):a string representation  of the text
    """
    print(Fore.BLUE + text)
    print(Style.RESET_ALL)

def create_file(filename,data):
    """
    Takes a filename and and data and creates and saves a file

    Args:
        filename (string): a string representation of the filename
        data (list): list of dictionaries representing movies
    """    
    user_file_input =input('would you like to save this list? (yes/no): ')
    if user_file_input == 'yes':
        with open(filename+".txt", "w",encoding="utf8") as f:
             for movie_info in data:
                if 'name' in movie_info:
                    f.write(f"Title:{movie_info['name']}\n\nSummary:\n\n{movie_info['overview']}\n\nRating:{str(movie_info['vote_average'])}\n================================\n\n")
                else:
                    f.write(f"Title:{movie_info['title']}\n\nSummary:\n\n{movie_info['overview']}\n\nRating:{str(movie_info['vote_average'])}\n================================\n\n")
        print_text_green("your file has been successfully saved")

def print_trending_shows(trending_shows):
    """
    Loops through list of dictionaries and prints the list of titles, summary and original language for trending shows 

    Args:
        trending_shows (list): a list of dictionaries containing the details of each show
    """    
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

def print_top_movies(top_movies):
    """
    Loops through list of dictionaries and prints the list of titles, summary and rating for top movies

    Args:
        top_movies (list): a list of dictionaries containing the details of each movie 
    """    
    for movie in top_movies:
        print('\n================================')
        print('Title: ' + movie['title'])
        print('Summary: ' + movie['overview'])
        print('Rating: ' + str(movie['vote_average']))

def print_upcoming_movies(upcoming_movies):
    """
    Loops through list of dictionaries and prints the list of titles, summary and release date for upcoming movies

    Args:
        upcoming_movies (list): a list of dictionaries containing the details of each upcoming movie
    """    
    for movie in upcoming_movies:
        print('\n================================')
        print('Title: ' + movie['title'])
        print('Summary: ' + movie['overview'])
        print('Release date: ' + str(movie['release_date']))