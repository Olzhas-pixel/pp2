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
#1
def cd(movie):
    
    return movie.get("imdb", 0) > 5.5

bc = {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"}
print("#1")
print(cd(bc))
#2
def ab(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

e = ab(movies)
print("#2")
for movie in e:
    
    print(movie)
    
#3 
def m(category, movies):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]


x = "Romance"
r = m(x, movies)
print("#3")
print(r)

#4
print("#4")
def ae(movies):
    if not movies:
        return 0  
    
    total_score = sum(movie["imdb"] for movie in movies)
    as2 = total_score / len(movies)
    
    return as2


as2 = ae(movies)
print("Average IMDB Score:", as2)

#5
print("#5")
def average_imdb_by_category(movies, category):
    category_movies = [movie["imdb"] for movie in movies if movie["category"].lower() == category.lower()]
    return sum(category_movies) / len(category_movies) if category_movies else 0


print(average_imdb_by_category(movies, "Romance"))
print(average_imdb_by_category(movies, "Thriller"))
print(average_imdb_by_category(movies, "Sci-Fi")) 
