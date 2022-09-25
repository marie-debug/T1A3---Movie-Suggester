import test_input
import helpers as hp
import pytest


def test_genre_dictionary():
    
    genre = test_input.genres_result
    result = hp.genre_dictionary(genre)
    expected_genre_dict = {'action': 28, 'adventure': 12, 'animation': 16, 'comedy': 35, 'crime': 80, 'documentary': 99, 'drama': 18, 'family': 10751, 'fantasy': 14,
                           'history': 36, 'horror': 27, 'music': 10402, 'mystery': 9648, 'romance': 10749, 'science fiction': 878, 'tv movie': 10770, 'thriller': 53, 'war': 10752, 'western': 37}
    assert result == expected_genre_dict


def test_print_trending_shows(capfd):

    hp.print_trending_shows(test_input.trending_shows['results'])
    out, err = capfd.readouterr()
    expected_output1 = '\n================================\nTitle: Star Wars: Andor\nSummary: test overview\nOriginal_language: en\n'
    expected_output2 = '\n================================\nTitle: Dahmer - Monster: The Jeffrey Dahmer Story\nSummary: Across more than a decade\nOriginal_language: en\n'
    assert out == expected_output1+expected_output2


def test_print_top_movies(capfd):

    hp.print_top_movies(test_input.top_movies['results'])
    out, err = capfd.readouterr()
    expected_output1 = '\n================================\nTitle: SK80\nSummary: When desire is stronger than physical strength\nRating: 10\n'
    expected_output2 = '\n================================\nTitle: Bugs\nSummary: After a virus decimates the wild rabbit populations\nRating: 10\n'
    assert out == expected_output1+expected_output2


def test_print_upcoming_movies(capfd):

    hp.print_upcoming_movies(test_input.upcoming_movies['results'])
    out, err = capfd.readouterr()
    expected_output1 = '\n================================\nTitle: Fall\nSummary: For best friends Becky and Hunter\nRelease date: 2022-08-11\n'
    expected_output2 = '\n================================\nTitle: Dragon Ball Super: Super Hero\nSummary: The Red Ribbon Army\nRelease date: 2022-06-11\n'
    assert out == expected_output1+expected_output2
