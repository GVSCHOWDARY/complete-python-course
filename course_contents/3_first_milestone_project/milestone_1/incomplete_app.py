# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

 
def a_movie():
# You may want to create a function for this code
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

def l_movies():
    for movie in movies:
        print_movie(movie)
        
def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")
          
def f_movies():
    title_name = input("What is the movie you are searching")
          
    for movie in movies:
        if movie["title"] == title_name:
            print_movie(movie)
# Create other functions for:
#   - listing movies
#   - finding movies
user_option = {
    "a"= a_movie,
    "l"= l_movies,
    "f"= f_movies
}

          
   
def menu():          
# And another function here for the user menu
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            pass
        elif selection == "l":
            pass
        elif selection == "f":
            pass
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)

menu()
# Remember to run the user menu function at the end!
