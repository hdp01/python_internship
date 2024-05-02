# importing all required libraries
import imdb
import datetime
import textwrap

# Function for searching movie
def search_movie():
    # gathering information from IMDb
    moviesdb = imdb.IMDb()# get input from user
    text = input("Enter the movie name: ")
    # passing input for searching movie
    movies = moviesdb.search_movie(text)

    print("Searching for " + text)
    if len(movies) == 0:
        print("No result found")
    else:
        print("I found these:")
        for movie in movies:
            title = movie['title']
            year = movie['year']
            # print title with releasing year
            print(f'{title}-{year}')

            info = movie.getID()
            movie = moviesdb.get_movie(info)

            title = movie['title']
            year = movie['year']
            rating = movie['rating']
            plot = movie['plot outline']

            # wrapping the plot summary to a specific width
            wrapped_plot = textwrap.fill(plot, width=80)

            # the below if-else is for past and future release
            if year < int(datetime.datetime.now().strftime("%Y")):
                print("\nMovie Information:")
                print(f'Title: {title}')
                print(f'Release Year: {year}')
                print(f'IMDB Rating: {rating}')
                print(f'Plot Summary: {wrapped_plot}\n')
                break

            else:
                print("\nMovie Information:")
                print(f'Title: {title}')
                print(f'Release Year: {year}')
                print(f'IMDB Rating: {rating}')
                print(f'Plot Summary: {wrapped_plot}\n')
                break
search_movie()