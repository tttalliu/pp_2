#task1
def imdb(movie):
    return movie['imdb']>5.5
movie={
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
}
print(imdb(movie))

#task2
def print_imdb_5_5(movies):
    return [movie for movie in movies if movie['imdb']>5.5]
movies=[
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
}]
list_5_5=print_imdb_5_5(movies)
print(list_5_5)

#task3
def print_category(movies, category):
    return [movie for movie in movies if movie['category']==category]
movies=[
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
}]
category_name="Suspense"
list_category=print_category(movies,category_name)
print(list_category)

#task4
def average_score(movies):
    total=sum([movie['imdb'] for movie in movies])
    if len(movies)==0:
        return 0
    return total/len(movies)
movies=[
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
}]
average=average_score(movies)
print(average)

#task5
def avg_for_category(movies,category):
    category_m=([movie['imdb'] for movie in movies if movie['category']==category])
    if len(category_m)==0:
        return 0
    return sum(category_m)/len(category_m)
movies=[
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
}]
category_name="Suspense"
avg_imdb=avg_for_category(movies,category_name)
print(avg_imdb)