# ---------------
# IMDB datasets preprocessing and database creation
# Weimiao Wu
# Date: 12/29/2018
# Last update: 12/13/2018
# ---------------


import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np


movie_basic = pd.read_csv('title.basics.tsv', sep='\t')
movie_basic_nona = movie_basic[movie_basic.startYear !='\\N']
movie_basic_nona = movie_basic_nona.dropna()
movie_basic.head(5)
movie_basic['titleType'].value_counts()
movie_basic['isAdult'].value_counts()
movie_basic.index[movie_basic['isAdult'] == 2018].tolist()
movie_basic.loc[4726667,:]

#drop movies with unknown year of production
na_startyear_index = movie_basic.index[movie_basic['startYear']=='\\N'].tolist()
movie_basic.loc[na_startyear_index,:]
movie_basic = movie_basic.drop(movie_basic.index[na_startyear_index])
movie_basic.shape
movie_basic['startYear'] = movie_basic['startYear'].astype('int')

movie_basic['startYear'].hist()

#subset year 1900-2000 movies
movies = movie_basic.loc[movie_basic['titleType'] == 'movie']
movie_19 = movies[movies['startYear'].between(1991, 1999, inclusive=True)]


#remove movie with missing value
movie_19 = movie_19[movie_19.runtimeMinutes != '\\N']
movie_19.shape
movie_19.head(10)
movie_19 = movie_19.drop(['endYear'], axis=1)
movie_19['startYear'].hist()
genres = movie_19["genres"].str.split(",", n = 0, expand = True) 
genres.columns = ['g1', 'g2', 'g3']
genres.replace(to_replace=[None], value=np.nan, inplace=True)
genres.replace(to_replace=['\\N'], value=np.nan, inplace=True)
genres_cat = list(set(genres.g1) | set(genres.g2)| set(genres.g3))

genres_table = pd.DataFrame(genres_cat[1:])
genres_table.columns = ["Genres_Name"]
print(genres_table)

# genres_table
gen_id = ['{}_{}'.format(a, b) for b in list(range(1,genres_table.shape[0]+1)) for a in ["gr"]]
genres_table['Genres_ID'] = gen_id

genres.replace(to_replace=[None], value=np.nan, inplace=True)
genres['g1'] = genres['g1'].map(genres_table.set_index('Genres_Name')['Genres_ID'])
genres['g2'] = genres['g2'].map(genres_table.set_index('Genres_Name')['Genres_ID'])
genres['g3'] = genres['g3'].map(genres_table.set_index('Genres_Name')['Genres_ID'])

genres['tconst'] = movie_19['tconst']
movie_genres = genres[['tconst', 'g1', 'g2', 'g3']]
movie_genres[:10]  # Genres_movie(movie_id, genres_ID (multivalue))

# add discription to genres
desc = pd.read_excel('genres_description.xlsx', header=None)
desc.columns = ['genres', 'desc']
genres_table['Description'] = genres_table['Genres_Name'].map(desc.set_index('genres')['desc'])
genres_table # Genres(genres_ID, genres_name, description)
genres_table.to_csv('genres_table.csv')
movie_genres.to_csv('movie_genres.csv')

# reading in LIngyi's dataset - cast_people
Cast_people = pd.read_csv('from_Lingyi/Cast_people.tsv', sep = "\t", header = 0)
Cast_people.columns
Cast_people = Cast_people[['Person_ID', 'Name', 'Birth Year', 'Death Year']]
print(Cast_people.shape)

# cast_re
Cast_re = pd.read_csv('from_Lingyi/Cast_re.tsv', sep = "\t", header = 0)
Cast_re.columns
Cast_re = Cast_re[['Movie_ID', 'Person_ID', 'characters', 'category']]

Crew_people = pd.read_csv('from_Lingyi/Crew_people.tsv', sep = "\t", header = 0)
Crew_people.columns
Crew_people = Crew_people[['Person_ID', 'Name', 'Birth Year', 'Death Year', 'Primary Profession']]

Crew_re = pd.read_csv('from_Lingyi/Crew_re.tsv', sep = "\t", header = 0)
Crew_re = Crew_re[['Movie_ID', 'Person_ID', 'Category']]

movie = pd.read_csv('from_LIngyi/movie.tsv', sep = "\t", header = 0)
movie = movie.drop(movie.columns[0], axis=1)
movie

rating = pd.read_csv('from_LIngyi/rating_new.csv')
rating = rating.drop(rating.columns[0], axis = 1)

title = pd.read_csv('from_LIngyi/title.tsv', sep = "\t", header = 0)
title = title.drop(title.columns[0], axis = 1)

#renaming variables
Cast_re.rename(columns={Cast_re.columns[3]: "roll"})
movie_genres.rename(columns={movie_genres.columns[0]: "Movie_ID"})


# Export to database

engine2 = sqlite3.connect('IMDB3.db')
#write dataframe to db
genres_table.to_sql('genres_table', con = engine2, index = False)
movie_genres.to_sql('genres_re', con = engine2,index = False)
Cast_people.to_sql('cast_people', con = engine2,index = False)
Cast_re.to_sql('cast_re', con = engine2,index = False)
Crew_people.to_sql('crew_people', con = engine2,index = False)
Crew_re.to_sql('crew_re', con = engine2,index = False)
movie.to_sql('movie', con = engine2,index = False)
rating.to_sql('rating', con = engine2,index = False)
title.to_sql('title', con = engine2,index = False)
engine2.close



