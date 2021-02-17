import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
###### helper functions. Use them when needed #######
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]
##################################################

##Step 1: Read CSV File

df=pd.read_csv('movie_dataset.csv')



##Step 2: Select Features

features=['genres','keywords','director','cast']

for feature in features:
	df[feature]=df[feature].fillna('')
##Step 3: Create a column in DF which combines all selected features
def combine_features(row):
	try:
	   return row['genres']+" " +row['keywords']+" "+row['director']+" "+row['cast']
	except:
		print('Error',row)

df['combined_features']=df.apply(combine_features,axis=1)
#print(df.head())
##Step 4: Create count matrix from this new combined column
cv=CountVectorizer()
count_matrix=cv.fit_transform(df['combined_features'])
##Step 5: Compute the Cosine Similarity based on the count_matrix
cosine_sim=cosine_similarity(count_matrix)



def recommend_movies(movie_user_likes):
	recommendation=[]
	## Step 6: Get index of this movie from its title
	index = get_index_from_title(movie_user_likes)
	similar_movies = list(enumerate(cosine_sim[index]))
	## Step 7: Get a list of similar movies in descending order of similarity score
	sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)

	## Step 8: Print titles of first 50 movies
	i = 0
	for movie in sorted_similar_movies:

		recommendation.append(get_title_from_index(movie[0]))
		i += 1
		if i > 50:
			return recommendation
			break


import json
columns={
	'data_columns':[col.lower() for col in df.original_title]
}
with open('columms.json','w') as f:
	f.write(json.dumps(columns))

if __name__=='__main__':
	movie_user_likes = str(input('Please enter a movie name:'))
	movies=recommend_movies(movie_user_likes)
	print(movies)