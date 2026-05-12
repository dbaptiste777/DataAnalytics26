list_name = "My favorite movies"
length = 5 

movie_1 = "The Incredibles"
movie_2 = "Eyes Wide Shut"
movie_3 = "Paid In Full"
movie_4 = "Madagascar"
movie_5 = "Shrek"


movies = [ 'The Incredibles', 'Eyes Wide Shut', 'Paid In Full', 'Madagascar', 'Shrek' ]

print("The list", movies, "includes my top", len(movies), "favorite movies")

print(sorted(movies)) #This printed the list alphabetically.

print(movies) #This prints the list as is.

print(movies.sort) #Message <built-in method sort of list object at 0x000001220643B700>

print(movies.sort()) #The output given is "none"

movies.append('The Notebook')

print(movies)




