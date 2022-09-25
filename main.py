from dotenv import load_dotenv
import pyfiglet
import helpers as hp
import api_request


def main():
    load_dotenv()

    INSTRUCTIONS = """
    [trend] Enter Trend to get top 10 trending movies and shows.

    [genre] Enter genre name eg horror, action to get top 10 movies and shows based on genres.

    [latest] Enter Latest to get top 10 upcoming movies and shows.

    [q] Enter q to quit.
    """

    genre_names = api_request.get_genres()

    user_input = ''

    welcome_message = pyfiglet.figlet_format(
        "Welcome to Movie suggestor, we help you find great shows")
    hp.print_text_blue(welcome_message)

    hp.print_text_green(INSTRUCTIONS)

    while user_input != 'q':
        user_input = input("\nWhat would you like to do?:  ").lower()

        if user_input == 'q':
            print("\nMay the Force be with you.\n")
            break

        expected_user_input = ['trend', 'genre', 'q', 'latest']
        if user_input not in expected_user_input:
            hp.print_text_green(INSTRUCTIONS)

        if user_input == 'genre':

            genre_input = ''

            while genre_input not in genre_names:
                genre_input = input(
                    "\n[2] Enter genre name eg horror, action to get top 10 movies and shows based on genres: ").lower()

                if genre_input == 'q':
                    print("\nMay the Force be with you.\n")
                    user_input = 'q'
                    break

                if genre_input in genre_names:
                    print(
                        f'\nYou have selected {genre_input} below is a list of top 10 {genre_input} movies available:\n ')
                    data = api_request.get_top_movies(genre_input)
                    hp.create_file('top movies', data)
                else:
                    hp.print_text_green(
                        'The genre selected is not available. Please select from list below.')
                    [hp.print_text_green(key)for key, value in genre_names.items()]

        elif user_input == 'trend':
            print(
                f'\nYou have selected {user_input} below is a list of top 10 trending movies available:\n ')

            data = api_request.get_trending_shows()
            hp.create_file('trending movies', data)
        elif user_input == 'latest':
            print(
                f'\nYou have selected {user_input} below is a list of top 10 upcoming movies:\n ')

            data = api_request.get_upcoming_movies()
            hp.create_file('upcoming movies', data)

    bye_message = pyfiglet.figlet_format(
        "Thanks again, we hope to see you soon ! Hasta la vista, baby.", font="slant")

    hp.print_text_blue(bye_message)


if __name__ == '__main__':
    main()
