import requests
# converts genrelist to genredictionary with genre names and id

def genre_dictionary(genres_result):
    genresList = genres_result['genres']
    genre_dict = {}
    for genre in genresList:
        genre_dict[genre['name'].lower()] = genre['id']
    return genre_dict

def get_data(url):
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