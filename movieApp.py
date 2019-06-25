#Import the class to instantiate movie objects
from movieClass import Movie

# Stores list of movie objects

listOfMovies=[]

# Function to print details of the movie

def PrintMovieDetails(movie):
    print("Name: "+movie.getName())
    print("Category: "+movie.getCategory())
    print("Description: "+movie.getDescription())
    print("Price: "+movie.getPrice())

# Search Function to look for movies

def SearchBasedOnNameOrCategory(searchString, listOfMovies):
    searchList=[]
    for m in listOfMovies:
        if(m.getName().lower()==searchString.lower()):
            searchList.append(m)
    
    return searchList   

def menu1():
    print("\n\nDisplay all movies")
    index = 0
    usrInput = ""
    while usrInput != "M":
        print("\nMovie "+str(index+1)+" of "+str(len(listOfMovies)))
        print("==============================")
        #Usage of function to display the movie details
        PrintMovieDetails(listOfMovies[index])

        print("==============================")
        print("Enter N for Next movie")
        print("Enter P for Previous movie")
        usrInput = input("Enter M to return to Main Menu\n")

        # Logic for usrInput
        if usrInput == "N":
            index += 1
        if index >= len(listOfMovies):
            index = 0
        elif usrInput == "P":
            index -= 1
        if index < 0:
            index = len(listOfMovies)-1

def menu2():
    print("\n\nDisplay movie full names for selection")
    usrInput = ""
    while True:
        for index in range(len(listOfMovies)):
            print(str(index+1)+". "+listOfMovies[index].getName())
			
        print("Enter M to return to Main Menu")
            
        usrInput = input("Please enter your selection\n")

        if usrInput == "M":
            break
        index = int(usrInput)-1
        print("\nMovie "+usrInput+" of "+str(len(listOfMovies)))
        print("==============================")
            #Usage of function to display the movie movie details
        PrintMovieDetails(listOfMovies[index])
          
        print("==============================\n")
        innerMenu = ""

        innerMenu = input("Enter M to return to Previous Menu. Any key continue.\n")
        if innerMenu == "M":
            break

# Usage of the searcg based function
def menu3():
    print("\n\nSearch based on Name or Category substring")
    usrInput = ""
    while True:
        searchString = input("Please enter your search input\n")
        trueSearch=SearchBasedOnNameOrCategory(searchString,listOfMovies)
        for search in trueSearch:
            PrintMovieDetails(search) 
        
        usrInput = "reset"
        while usrInput != "1" and usrInput != "2" :
            print("1. Search again")
            usrInput = input("2. Return to Main Menu\n")

        if usrInput == "2":
            break

#Read movies from  input file

file=open('movieData.txt')
lines=file.readlines()

for data in lines:
    data=data.replace("\n","")
    cols=data.split(">")
    name=cols[0]
    category=cols[1] 
    description=cols[2]
    price=cols[3]
    m=Movie(name,category,description,price)
    listOfMovies.append(m)

file.close()

while True:
    print("Main Menu")
    print("----------")
    print("1. Display all movies")
    print("2. Display movie full names for selection")
    print("3. Search based on Name or Category substring")
    print("Q. Enter Q to quit")

    menuSelection = input("Please input your selection\n")
    if menuSelection == "Q":
        break
    print("You have selected "+menuSelection+".. ",end="")

    if menuSelection == "1":
        #include exception handling for index error
        try:
            menu1()
        except IndexError:
            print("IndexError occurred")
       
    if menuSelection == "2":
        #include exception handling for index error
        try:
            menu2()
        except IndexError:
            print("IndexError occurred")

    if menuSelection == "3":
        menu3()

