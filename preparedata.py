import scraper
import csv
import time

def read_movie_list(filename):
    """ Reads movies from file where text is format: Title (year), ImdbID """
    """ param - `filename` - name of input file """
    movies = []

    rate_limit = 30
    limit_count = 0

    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            print(row)
            if limit_count == rate_limit:
                break
                #time.sleep(10)
            nude_info = scraper.fetch_nudity_info(row[1].replace('tt', ''), 'movie')
            movies.append({'title': row[0], 'description': ' '.join(nude_info)})
            limit_count += 1
    return movies

def write_movies_with_nude_info_to_csv(movies, outputFile):
    """ Writes movie info into a csv """
    """ param 'movies' - array of movies alongside their respective nudity information """
    """ param 'outputFile' - desired filename of generated csv file """
    csv_columns = ['title', 'description']
    try:
        with open(outputFile, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter='|')
            writer.writeheader()
            for data in movies:
                writer.writerow(data)
    except IOError:
        print("I/O error")

## TODO: Move/call this function if wanting to make this an executable script
def generate_movie_nudity_csv_from_file(inputFile, outputFile): 
    movies = read_movie_list(inputFile)
    write_movies_with_nude_info_to_csv(movies, outputFile)

# generate_movie_nudity_csv_from_file('import_non_nude.csv', 'non_nude_movies.csv')