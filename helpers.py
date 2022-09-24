import requests

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
