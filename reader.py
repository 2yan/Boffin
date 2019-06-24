import numpy as np
import pandas as pd


    

def gen_path():
    with open("outfile.txt", 'r') as f:
        raw = f.read()
    
    raw = raw.split('\n')
    x = []
    y = []
    for i, row in enumerate( raw[:-1]):
        splt = row.split(',')
        print(i, '-' ,splt[0],' --- ', splt[1])
        x.append(float(splt[0]))
        y.append(float(splt[1]))



    return [x,y]
        




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
    
