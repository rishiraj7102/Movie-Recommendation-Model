import pickle
import json
import numpy as np
__movie_names=None
__recommended=None
__data_columns=None
import movie_recommender_starter
def load_movies():
    global __movie_names
    with open('columms.json','r') as f:
        data_columns=json.load(f)['data_columns']
        __movie_names=data_columns[:]
def get_movie_names():
    return __movie_names




if __name__=='__main__':
    load_movies()