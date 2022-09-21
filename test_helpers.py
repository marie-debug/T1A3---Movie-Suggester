import test_input
import helpers as hp
import test_expected_output as expected


def test_genre_dictionary():
    assert hp.genre_dictionary(test_input.genres_result) == expected.genre_dict
