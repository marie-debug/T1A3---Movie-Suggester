
# converts genrelist to genredictionary with genre names and id

def genre_dictionary(genres_result):
    genresList = genres_result['genres']
    genre_dict = {}
    for genre in genresList:
        genre_dict[genre['name'].lower()] = genre['id']
    return genre_dict

