class Movie():
    # Doc string for my function:
    """
    This Class defined to store favorite movies including :
    Title , Poster Image , Trailer's youtube link.
    >> This class called :
    ** Variable(e.g your_Movie_Name) = Movie(Title,Poster_image,trailer_link)

    NOTE THAT >> All arguments in this class are strings !!
              >> Before use this class you must import it in your code :
                 ** import Movies **
    """
    # defiine __init__ function:
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title  # Movie's Name
        self.poster_image_url = poster_image  # Box Art / Movie's Poster image
        self.trailer_youtube_url = trailer_youtube  # Movie's trailer video
