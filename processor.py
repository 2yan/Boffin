import scipy
import pandas as pd
import numpy as np
from scipy.ndimage.filters import gaussian_filter1d



def smooth_data(data):
    data['x'] = gaussian_filter1d(data['x'], sigma = 1)
    data['y'] =  gaussian_filter1d(data['y'], sigma = 1)
    return data
    
def zero_and_one(x):
    x = x.max() - x
    x = x - x.min()
    x = x/x.max()
    return x

def fit_to_universe(data):
    data['x'] = zero_and_one(data['x'])
    data['y'] = zero_and_one(data['y'])
    return data


def reduce_obs(data, amt = 10000):
    if len(data) < amt:
        return data

    data['i'] = data.index/(len(data)/amt)
    data['i'] = data['i'].apply(int)
    data = data.groupby('i').mean()
    return data 
