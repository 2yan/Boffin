from adxl345 import ADXL345
import pandas as pd
import numpy as np

s = ADXL345()



def raw_read():
    ans = s.get_axes(False)
    return ans



def get_data(samples = 1):
    if samples == 1:
        return raw_read()
    xs = []
    ys = []
    zs = []

    amt = samples 
    for num in range(0, amt):
        ans = raw_read()
        x = ans['x'] 
        y = ans['y']
        z = ans['z']
        
        xs.append(x)
        ys.append(y)
        zs.append(z)
    xs = np.mean(xs)
    ys = np.mean(ys)
    zs = np.mean(zs)

    result = {'x':xs, 'y':ys, 'z':zs}
    return result

     
    

if __name__ == '__main__':

    while True:
        ans = get_data()
        x = ans['x'] 
        y = ans['y']
        z = ans['z']

        text = "{:,.4f} |  {:,.4f}  |  {:,.4f}".format(x, y, z)
        print(text)
