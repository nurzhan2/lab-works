movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


# task 1 

def f( movie ):
    return movie["imdb"] > 5.5 

print ( f(movies[-2]) )

# task 2 

def f2 ( movies ):
    for i in movies:
        if ( i["imdb"] > 5.5 ):
            print ( i ["name"] )
    
    return 0

f2 ( movies )

#task 3

def f3 ( movies , category):
    for i in movies :
        if i["category"] == category :
            print ( i ["name"] )
    
    return 0            

category = input ( "category : " )
f3(movies , category)

#task 4 

def average_imdb_by_names():
    movie_names_input = input("Enter movie names separated by commas: ")
    
    movie_names = [name.strip() for name in movie_names_input.split(",")]

    
    total_score = 0
    found_count = 0
    
    for name in movie_names:
        for movie in movies:  
            if movie["name"] == name:
                total_score += movie["imdb"]
                found_count += 1
                break 
    
    if found_count == 0:
        return 0.0 
    return total_score / found_count

avg_score = average_imdb_by_names()

print(f"Average IMDB score: {avg_score:.2f}")

#task 5 

def f5( movies , category ):
    movieCount = 0 
    movieImdb = 0 

    for i in movies:
        if i["category"] == category:
            movieCount+=1
            movieImdb+=i["imdb"]
    return movieImdb/movieCount

category = input("Category : ")
print ( f5( movies, category) )