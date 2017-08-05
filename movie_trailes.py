# To import: Movie() Class in our code
import movie
# To import: open_movies_page() function
import fresh_tomatoes

# List Movies Titles
titles = ["White House Down",  # First Movie Title : titles[0] and so on
          "Shaun The Sheep",
          "The Jungle Book",
          "The Wanted 18",
          "Amreeka",
          "Paradise Now"]

# List Movies poster imades By the same order in titles
posters = ["http://www.impawards.com/2013/posters/white_house_down_ver9.jpg",
           "http://sim03.in.com/62/0f18509be625de1f3ce13c48e32d280d_ft_m.png",
           "http://maxcdn.dardarkom.com/up/uploads/1460598611824.jpg",
           "http://www.arabamericanmuseum.org/umages/TW18site.png",
           "http://www.webdo.tn/wp-content/uploads/2016/12/Amreeka.jpg",
           "http://www.impawards.com/2005/posters/paradise_now_ver5.jpg"]

# List Movies Trailer Youtube links in the same order in titles
trailer_links = ["https://www.youtube.com/watch?v=4AXbiCdmXgw",
                 "https://www.youtube.com/watch?v=tQvwiOWpj7o",
                 "https://www.youtube.com/watch?v=5mkm22yO-bs",
                 "https://www.youtube.com/watch?v=pnIpxHsqB2o",
                 "https://www.youtube.com/watch?v=DRKa2MLkKLA",
                 "https://www.youtube.com/watch?v=Xi9yiGePxKw"]

# use Movie() Class to all movies
movies = []  # Empty List

if(len(titles) == len(posters) == len(trailer_links)):
    for i in range(0, len(titles)):
        # e.g:obj = movie.Movie(titles[0],posters[0],trailer_links[0])
        obj = movie.Movie(titles[i], posters[i], trailer_links[i])
        # USE append function to add Movies in (moves empty list)
        movies.append(obj)
        # NOW (moves list) don't empty
else:
    print("There's one Movie or more DONT have all details")
# use open_movies_page() function to display movies in web page
fresh_tomatoes.open_movies_page(movies)
