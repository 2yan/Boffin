import numpy as np
import pandas as pd


    

       




def get_data():
    raw_data = pd.read_csv('results.txt')
    raw_data = raw_data.sort_values('time')
    
    x = raw_data['lat']
    y = raw_data['long']


    data = pd.DataFrame(index = range(len(x)))
    data['x'] = x
    data['y'] = y
    data['accel'] = raw_data['x_accel'] + raw_data['y_accel'] + raw_data['z_accel']
    
    data['brake'] = data['accel']
    mask = data['accel'] <= 0
    data.loc[mask, 'accel'] = 0
    data.loc[~mask, 'brake'] = 0
    
    
    
    return data
    
