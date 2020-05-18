import scraper
import csv
import time

movies = []

rate_limit = 30
limit_count = 0

with open('import.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(row)
        if limit_count == rate_limit:
            break
            #time.sleep(10)
        nude_info = scraper.fetch_nudity_info(row[1].replace('tt', ''), 'movie')
        movies.append({'title': row[0], 'description': ' '.join(nude_info)})
        limit_count += 1

""" with open('radarr-export.csv', 'r') as in_file:
    lines = in_file.readlines()

for line in lines[1:]:
    tokens = line.split(',')
    movies.append({'title': tokens[0], 'description': '\n'.join(scraper.fetch_nudity_info(tokens[1], 'movie'))})
 """
print(movies[0:5])


csv_columns = ['title','description']
csv_file = "movies.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter='|')
        writer.writeheader()
        for data in movies:
            writer.writerow(data)
except IOError:
    print("I/O error")