from imdb import IMDb, helpers

import scraper
import parse
import csv
import time




#nudity_info = scraper.fetch_nudity_info('0356150', 'movie')
#print('Nudity: {0}'.format(nudity_info))

#is_nudity, nudity_score = parse.parse_nudity(nudity_info)
#print('Is Nudity: {0}. Possiblity Correct: {1}'.format(is_nudity, nudity_score))



with open('movies.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='|', quotechar='"')
    next(reader, None)  # skip the headers
    for row in reader:
        if len(row) is 2:
            is_nudity, nudity_score = parse.parse_nudity(row[1])
            print('Movie: {0}'.format(row[0]))
            print('Is Nudity: {0}. Possiblity Correct: {1}'.format(is_nudity, nudity_score))






""" 
# create an instance of the IMDb class
ia = IMDb()

movies = ia.search_movie('Beanpole (2019)', 1)

movie_parental_sex_url = 'https://www.imdb.com/title/tt{0}/parentalguide'
url = movie_parental_sex_url.format(10199640)
something = helpers.get_byURL(url)



movie = ia.get_movie('10199640')
print(movie.keys())
for genre in movie['genres']:
    print(genre)

# print the genres of the movie
for movie in movies:
    print('Title: {0}'.format(movie['title']))
    print('ID: {0}'.format(movie['id']))
    print('Genres:')
    for genre in movie['genres']:
        print(genre) """