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
    try:
        response = requests.get(url).json()
        data = response['results'][:11]
    except requests.ConnectionError:
        print("OOPS!! Connection Error. Make sure you are connected to Internet.\n")
    except requests.Timeout:
        print("OOPS!! Timeout Error")
    except requests.RequestException:
        print("OOPS!! General Error")
    finally:
        print("Please try again.")
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