
#expected output result after hitting the genre api endpoint#
genres_result = {'genres':
                 [
                     {'id': 28, 'name': 'Action'},
                     {'id': 12, 'name': 'Adventure'},
                     {'id': 16, 'name': 'Animation'},
                     {'id': 35, 'name': 'Comedy'},
                     {'id': 80, 'name': 'Crime'},
                     {'id': 99, 'name': 'Documentary'},
                     {'id': 18, 'name': 'Drama'},
                     {'id': 10751, 'name': 'Family'},
                     {'id': 14, 'name': 'Fantasy'},
                     {'id': 36, 'name': 'History'},
                     {'id': 27, 'name': 'Horror'},
                     {'id': 10402, 'name': 'Music'},
                     {'id': 9648, 'name': 'Mystery'},
                     {'id': 10749, 'name': 'Romance'},
                     {'id': 878, 'name': 'Science Fiction'},
                     {'id': 10770, 'name': 'TV Movie'},
                     {'id': 53, 'name': 'Thriller'},
                     {'id': 10752, 'name': 'War'},
                     {'id': 37, 'name': 'Western'}
                 ]
                 }

#expected output result after hitting the top movies api endpoint#
top_movies = {
    'page': 1,
    'results': [
        {
            'adult': False,
            'backdrop_path': None,
            'genre_ids': [16, 12, 35, 10751],
            'id': 1025488,
            'original_language': 'en',
            'original_title': 'SK80',
            'overview': 'When desire is stronger than physical strength',
            'popularity': 1.055,
            'poster_path': '/2RPcTudkd7CM2BCCQLYpUJpoVQc.jpg', 'release_date': '2022-07-06',
            'title': 'SK80',
            'video': False,
            'vote_average': 10,
            'vote_count': 1
        },
        {
            'adult': False,
            'backdrop_path': '/mdE69QWOkfHx3l2tG8gvC5jhhfN.jpg',
            'genre_ids': [12],
            'id': 1024637,
            'original_language': 'en',
            'original_title': 'Bugs',
            'overview': 'After a virus decimates the wild rabbit populations',
            'popularity': 0.6,
            'poster_path': '/rg9W9WpUeyT6fDEpUYhTIwcpN8W.jpg',
            'release_date': '2021-11-01',
            'title': 'Bugs',
            'video': False,
            'vote_average': 10,
            'vote_count': 1
        }
    ],
    'total_pages': 920,
    'total_results': 18398
}

#expected output result after hitting the trending shows api endpoint#
trending_shows = {'page': 1,
'results': [
    {'adult': False,
    'backdrop_path': '/3hPKf2eriMi6B2L5brfQH0A7MNe.jpg',
     'id': 83867,
      'name': 'Star Wars: Andor',
       'original_language': 'en',
       'original_name': 'Star Wars: Andor',
       'overview': 'test overview',
       'poster_path': '/59SVNwLfoMnZPPB6ukW6dlPxAdI.jpg', 'media_type': 'tv',
       'genre_ids': [10765, 10759, 10768],
       'popularity': 180.762,
       'first_air_date': '2022-09-21',
        'vote_average': 9.25,
         'vote_count': 12,
         'origin_country': ['US']
    },
    {'adult': False,
     'backdrop_path': '/5AzjmGoqRNGytd8bOKoDcWxhjV2.jpg', 
     'id': 113988, 'title': 'Dahmer - Monster: The Jeffrey Dahmer Story', 'original_language': 'en', 'original_name': 'Dahmer - Monster: The Jeffrey Dahmer Story', 'overview': 'Across more than a decade', 'poster_path': '/qAv0UoAQVZWd6HGc83fsli1aKmo.jpg', 'media_type': 'tv', 'genre_ids': [18, 80], 'popularity': 43.821,
      'first_air_date': '2022-09-21',
       'vote_average': 8.9,
        'vote_count': 11,
         'origin_country': ['US']
         },
    ], 'total_pages': 1000, 'total_results': 20000}       

#expected output result after hitting the upcoming movies endpoint#
upcoming_movies = {

    'dates': {'maximum': '2022-10-19', 'minimum': '2022-09-28'},
     'page': 1,
     'results':
     [
        {
            'adult': False,
            'backdrop_path': '/2RSirqZG949GuRwN38MYCIGG4Od.jpg',
             'genre_ids': [53],
             'id': 985939,
              'original_language': 'en',
              'original_title': 'Fall',
              'overview': 'For best friends Becky and Hunter',
              'popularity': 6633.214,
               'poster_path': '/spCAxD99U1A6jsiePFoqdEcY0dG.jpg',
               'release_date': '2022-08-11',
               'title': 'Fall',
                'video': False,
                'vote_average': 7.4,
                'vote_count': 792

                },
                 {
                    'adult': False,
                    'backdrop_path': '/ugS5FVfCI3RV0ZwZtBV3HAV75OX.jpg',
                    'genre_ids': [16, 878, 28],
                    'id': 610150,
                    'original_language': 'ja',
                     'original_title': 'ドラゴンボール超 スーパーヒーロー',
                      'overview': 'The Red Ribbon Army',
                       'popularity': 2783.286,
                        'poster_path': '/rugyJdeoJm7cSJL1q4jBpTNbxyU.jpg',
                         'release_date': '2022-06-11',
                         'title': 'Dragon Ball Super: Super Hero',
                          'video': False,
                          'vote_average': 8,
                          'vote_count': 1677
                          }

                          ],
                          'total_pages': 24,
                           'total_results': 461
                           }
