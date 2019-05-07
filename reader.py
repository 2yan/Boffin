import numpy as np
import pandas as pd


    

def gen_path():
    
    def rng(chance = .02):
        return np.random.random() <= chance
        
    start = 0, 0 
    length = 400
    
    x_delta = np.random.random(length)
    y_delta = np.random.random(length)
    
    x = [start[0]]
    y = [start[1]]
    
    switch_x = False
    switch_y = False
    
    for i in range(1,length):
        
        if rng():
            switch_x = not switch_x
        if rng():
            switch_y = not switch_y
            
        if switch_x:
            new_x = x[i-1] + x_delta[i]
        else :
            new_x = x[i-1] - x_delta[i]
        if switch_y:
            new_y = y[i-1] + y_delta[i]
        else :
            new_y = y[i-1] - y_delta[i]
            
            
        x.append(new_x)
        y.append(new_y)
    
    return np.abs([x,y])
        




def get_data():    
    x,y = gen_path()
    data = pd.DataFrame(index = range(len(x)))
    data['x'] = x
    data['y'] = y
    data['accel'] = np.sin(data.index)
    data['brake'] = data['accel']
    mask = data['accel'] <= 0
    data.loc[mask, 'accel'] = 0
    data.loc[~mask, 'brake'] = 0
    
    
    
    return data
    