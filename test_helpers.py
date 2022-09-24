import test_input
import helpers as hp
import test_expected_output as expected


def test_genre_dictionary():
    genre= test_input.genres_result
    result=hp.genre_dictionary(genre)
    assert result == expected.genre_dict


