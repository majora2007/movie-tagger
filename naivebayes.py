from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import fetch_20newsgroups
from sklearn import metrics
from pprint import pprint
import sklearn.datasets as skd
import pandas as pd
import csv
import re

def file_into_dataframe(file, category, label):
    df = pd.read_csv(file, sep = "|")
    df['category'] = category
    df['label'] = label
    df['description'] = df['description'].astype(str)
    df['description'] = df['description'].apply(lambda x: cleanup_nudity_description_text(x))
    return df

def generate_dataframe():
    return pd.concat([file_into_dataframe('nude_movies.csv', 'contains_nudity', 1), file_into_dataframe('non_nude_movies.csv', 'no_nudity', 0)])

def cleanup_nudity_description_text(text):
    for char in ['.', '"', ",", ":"]:
        text = text.replace(str(char), ' ')
    return text.strip()

def naive_bayes():
    df = generate_dataframe()
    count_vect = CountVectorizer()
    tfidf_transformer = TfidfTransformer()

    x_train = count_vect.fit_transform(df['description'].tolist())
    x_train_tfidf = tfidf_transformer.fit_transform(x_train)

    trained_nb = MultinomialNB().fit(x_train_tfidf, df['label'])
    

    real_data_df = file_into_dataframe('movies.csv', 'unknown', 4)
    test_x_counts = count_vect.transform(real_data_df['description'].tolist())
    test_x_tfidf = tfidf_transformer.transform(test_x_counts)
    results = trained_nb.predict(test_x_tfidf)
    for idx, elem in enumerate(real_data_df['title'].tolist()):
        print('{}: {}'.format(elem, bool_to_nudity(results[idx])))

def bool_to_nudity(boolean):
    if boolean:
        return 'Nudity'
    return 'No Nudity'



naive_bayes()