import fresh_tomatoes
from movies import Movie

# Creating Movie objects
movie1 = Movie("Get Out", "http://www.trbimg.com/img-57f4386d/turbine/" \
                + "la-et-hc-get-out-horror-peele-20161004-snap",
                "https://www.youtube.com/watch?v=A2JbO9lnVLE")
movie2 = Movie("Logan", "http://t1.gstatic.com/images?q=tbn:ANd9GcRPo" \
                + "MqL1vglrh7OF_69pT8gYMYnYaq1r7WfPMcD587V9uOR_hW2",
                "https://www.youtube.com/watch?v=Div0iP65aZo")
movie3 = Movie("Days of Future Past", "http://t3.gstatic.com/images?q=tbn:" \
                + "ANd9GcSp1xUUrh6IW4gwa8j7p8WxU7Yt21mWhLVwZ5CejaXF6KsrOtjs",
                "https://www.youtube.com/watch?v=pK2zYHWDZKo")

# Create list of movies to feed into the open_movies_page function
list = (movie1, movie2, movie3)

# Call function from fresh_tomatoes to open page with given movies
fresh_tomatoes.open_movies_page(list)
