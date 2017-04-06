class Movie(object):
    """
    Movie object that holds a title, image url, and youtube url
    The constructor takes those respective arguments
    """
    def __init__(self, title, image_url, youtube_url):
        self.title = title
        self.poster_image_url = image_url
        self.trailer_youtube_url = youtube_url
