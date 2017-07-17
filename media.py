import webbrowser


class Movie():

    """This class Movie stores movie data such as movie_title, movie_storyline,
     poster_image, trailer_youtube

    """

    def __init__(self, movie_title, release_dates, movie_storyline,
                 poster_image, trailer_youtube):
        """function __init__ is called to initialize or create space in memory for
        new instance, here is for toy_story.

        """
        self.title = movie_title
        self.release_dates = release_dates
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ show_trailer() is a instance method."""

        webbrowser.open(self.trailer_youtube_url)
